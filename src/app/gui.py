import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QTextEdit,
)

from src.image.preprocessing import (
    load_image,
    convert_to_grayscale,
    image_to_array,
)

from src.encryption.pipeline import (
    encrypt_array,
    decrypt_array,
)

from src.security_analysis import (
    analyze_security,
    analyze_key_sensitivity,
    analyze_key_space,
)

from src.analysis.metrics import (
    analyze_differential,
)

from src.analysis.histogram import (
    calculate_histogram,
    histogram_uniformity_score,
)

from src.encryption.quantum_keystream import (
    generate_quantum_bits,
)

from src.analysis.quantum_metrics import (
    total_variation_distance,
)


# ============================================================
# APPLICATION CONSTANTS
# ============================================================

APP_TITLE = "Quantum-Inspired Image Encryption"

DEFAULT_KEY = "QuantumImageKey123"

RESULTS_DIR = Path("results")

GUI_GRAYSCALE = RESULTS_DIR / "gui_grayscale_preview.png"
GUI_ENCRYPTED = RESULTS_DIR / "gui_encrypted.png"
GUI_DECRYPTED = RESULTS_DIR / "gui_decrypted.png"



# ============================================================
# UI THEME
# ============================================================

COLORS = {
    "bg": "#0B1020", "surface": "#111827", "surface_alt": "#172033",
    "surface_hover": "#1D2940", "border": "#26344D", "text": "#E8EEF7",
    "muted": "#8FA1B8", "cyan": "#22D3EE", "cyan_dark": "#0891B2",
    "violet": "#8B5CF6", "violet_dark": "#6D28D9", "green": "#34D399",
    "green_dark": "#059669", "amber": "#FBBF24", "red": "#FB7185",
}

APP_STYLE = f"""
QWidget {{ background-color: {COLORS["bg"]}; color: {COLORS["text"]}; font-family: "Segoe UI"; font-size: 11px; }}
QMainWindow {{ background-color: {COLORS["bg"]}; }}
QGroupBox {{ background-color: {COLORS["surface"]}; border: 1px solid {COLORS["border"]}; border-radius: 12px; margin-top: 14px; padding: 18px 12px 12px 12px; font-weight: 700; color: {COLORS["cyan"]}; }}
QGroupBox::title {{ subcontrol-origin: margin; left: 14px; padding: 0 7px; color: {COLORS["cyan"]}; background-color: {COLORS["surface"]}; }}
QTabWidget::pane {{ border: 1px solid {COLORS["border"]}; border-radius: 10px; background-color: {COLORS["surface"]}; top: -1px; }}
QTabBar::tab {{ background-color: {COLORS["surface_alt"]}; color: {COLORS["muted"]}; border: 1px solid {COLORS["border"]}; border-bottom: none; padding: 10px 18px; margin-right: 3px; border-top-left-radius: 8px; border-top-right-radius: 8px; }}
QTabBar::tab:selected {{ background-color: {COLORS["surface"]}; color: {COLORS["cyan"]}; border-top: 2px solid {COLORS["cyan"]}; }}
QTabBar::tab:hover {{ color: {COLORS["text"]}; background-color: {COLORS["surface_hover"]}; }}
QPushButton {{ background-color: {COLORS["surface_alt"]}; color: {COLORS["text"]}; border: 1px solid {COLORS["border"]}; border-radius: 8px; padding: 9px 15px; font-weight: 700; }}
QPushButton:hover {{ background-color: {COLORS["surface_hover"]}; border-color: {COLORS["cyan"]}; }}
QPushButton:pressed {{ background-color: {COLORS["cyan_dark"]}; }}
QPushButton:disabled {{ background-color: #101827; color: #526176; border-color: #1C2738; }}
QLineEdit, QTextEdit, QTableWidget {{ background-color: #0D1524; color: {COLORS["text"]}; border: 1px solid {COLORS["border"]}; border-radius: 8px; selection-background-color: {COLORS["violet_dark"]}; selection-color: white; }}
QLineEdit {{ padding: 8px 10px; }}
QLineEdit:focus, QTextEdit:focus {{ border: 1px solid {COLORS["cyan"]}; }}
QHeaderView::section {{ background-color: {COLORS["surface_alt"]}; color: {COLORS["cyan"]}; border: none; border-bottom: 1px solid {COLORS["border"]}; padding: 8px; font-weight: 700; }}
QTableWidget {{ gridline-color: {COLORS["border"]}; alternate-background-color: #101A2B; }}
QTableWidget::item {{ padding: 6px; }}
QTableWidget::item:selected {{ background-color: {COLORS["violet_dark"]}; }}
QScrollArea {{ border: none; background-color: {COLORS["bg"]}; }}
QScrollBar:vertical {{ background: {COLORS["surface"]}; width: 10px; margin: 2px; }}
QScrollBar::handle:vertical {{ background: {COLORS["border"]}; border-radius: 5px; min-height: 30px; }}
QScrollBar::handle:vertical:hover {{ background: {COLORS["cyan_dark"]}; }}
"""

# ============================================================
# IMAGE PREVIEW
# ============================================================

class ImagePreview(QLabel):

    def __init__(self, placeholder="Image"):

        super().__init__()

        self.placeholder = placeholder
        self.current_pixmap = None

        self.setText(placeholder)

        self.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.setMinimumSize(
            210,
            210
        )

        self.setStyleSheet(
            """
            QLabel {
                border: 1px solid #26344D;
                border-radius: 12px;
                background-color: #0D1524;
                color: #6F8098;
                padding: 8px;
            }
            """
        )

    def set_image(self, image_path):

        pixmap = QPixmap(
            str(image_path)
        )

        if pixmap.isNull():

            self.current_pixmap = None
            self.clear()
            self.setText(
                "Unable to load image"
            )

            return

        self.current_pixmap = pixmap

        self.update_preview()

    def update_preview(self):

        if self.current_pixmap is None:
            return

        scaled = self.current_pixmap.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.setPixmap(
            scaled
        )

    def clear_image(self):

        self.current_pixmap = None

        self.clear()

        self.setText(
            self.placeholder
        )

    def resizeEvent(self, event):

        super().resizeEvent(
            event
        )

        self.update_preview()


# ============================================================
# METRIC CARD
# ============================================================

class MetricCard(QFrame):

    def __init__(
        self,
        title,
        value="—",
        description=""
    ):

        super().__init__()

        self.setFrameShape(
            QFrame.Shape.StyledPanel
        )

        self.setStyleSheet(
            """
            QFrame {
                background-color: #111827;
                border: 1px solid #26344D;
                border-radius: 11px;
                border-left: 3px solid #8B5CF6;
            }
            """
        )

        layout = QVBoxLayout()

        title_label = QLabel(
            title
        )

        title_label.setStyleSheet(
            """
            QLabel {
                color: #8FA1B8;
                font-size: 10px;
                font-weight: 800;
                letter-spacing: 0.6px;
            }
            """
        )

        self.value_label = QLabel(
            value
        )

        self.value_label.setStyleSheet(
            """
            QLabel {
                color: #E8EEF7;
                font-size: 21px;
                font-weight: 800;
            }
            """
        )

        description_label = QLabel(
            description
        )

        description_label.setWordWrap(
            True
        )

        description_label.setStyleSheet(
            """
            QLabel {
                color: #777777;
                font-size: 10px;
            }
            """
        )

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            self.value_label
        )

        if description:

            layout.addWidget(
                description_label
            )

        self.setLayout(
            layout
        )

    def set_value(self, value):

        self.value_label.setText(
            str(value)
        )


# ============================================================
# MAIN WINDOW
# ============================================================

class QuantumImageEncryptionGUI(QMainWindow):

    def __init__(self):

        super().__init__()

        # ----------------------------------------------------
        # Application state
        # ----------------------------------------------------

        self.selected_image_path = None

        self.original_image = None
        self.grayscale_image = None

        self.original_array = None
        self.encrypted_array = None
        self.decrypted_array = None

        self.encrypted_image_path = None
        self.decrypted_image_path = None

        self.security_results = None
        self.key_sensitivity_results = None
        self.key_space_results = None

        self.performance_results = None
        self.quantum_performance_results = None
        self.noise_results = None

        # ----------------------------------------------------
        # Window
        # ----------------------------------------------------

        self.setWindowTitle(
            APP_TITLE
        )

        self.setMinimumSize(
            1350,
            900
        )

        QApplication.instance().setStyleSheet(APP_STYLE)

        self.resize(
            1450,
            950
        )

        self.setup_ui()

    # ========================================================
    # STATUS / UI HELPERS
    # ========================================================

    def set_status(self, text, color=None):
        upper = text.upper()
        if color is None:
            if "ERROR" in upper or "FAILED" in upper:
                color = COLORS["red"]
            elif "COMPLETE" in upper or "VERIFIED" in upper or "READY" in upper:
                color = COLORS["green"]
            elif any(word in upper for word in ("RUNNING", "ENCRYPTING", "DECRYPTING", "ANALYZING", "TESTING")):
                color = COLORS["amber"]
            else:
                color = COLORS["cyan"]
        self.status_label.setText(text)
        self.status_label.setStyleSheet(f"QLabel {{ color: {color}; font-weight: 800; padding: 4px 10px; }}")

    # ========================================================
    # MAIN UI
    # ========================================================

    def setup_ui(self):

        central = QWidget()

        self.setCentralWidget(
            central
        )

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            18,
            14,
            18,
            14
        )

        main_layout.setSpacing(
            8
        )

        # ----------------------------------------------------
        # Header
        # ----------------------------------------------------

        header_layout = QVBoxLayout()

        title = QLabel(
            "QUANTUM-INSPIRED IMAGE ENCRYPTION"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)

        title.setFont(
            title_font
        )

        title.setStyleSheet(
            f"""QLabel {{ color: {COLORS["text"]}; padding: 6px; letter-spacing: 1px; }}"""
        )

        subtitle = QLabel(
            "Image encryption using quantum-circuit-derived keystream generation"
        )

        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        subtitle.setStyleSheet(
            """
            QLabel {
                color: #888888;
                font-size: 12px;
            }
            """
        )

        self.status_label = QLabel(
            "● READY"
        )

        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.status_label.setStyleSheet(
            """
            QLabel {
                color: #34D399;
                font-weight: 800;
            }
            """
        )

        header_layout.addWidget(
            title
        )

        header_layout.addWidget(
            subtitle
        )

        header_layout.addWidget(
            self.status_label
        )

        main_layout.addLayout(
            header_layout
        )

        # ----------------------------------------------------
        # Tabs
        # ----------------------------------------------------

        self.tabs = QTabWidget()

        self.tabs.addTab(
            self.create_demo_tab(),
            "Encryption Demo"
        )

        self.tabs.addTab(
            self.create_security_tab(),
            "Security Analysis"
        )

        self.tabs.addTab(
            self.create_performance_tab(),
            "Performance"
        )

        self.tabs.addTab(
            self.create_noise_tab(),
            "Quantum Noise"
        )

        self.tabs.addTab(
            self.create_about_tab(),
            "Architecture"
        )

        main_layout.addWidget(
            self.tabs
        )

        central.setLayout(
            main_layout
        )

    # ========================================================
    # ENCRYPTION DEMO TAB
    # ========================================================

    def create_demo_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()

        layout.setSpacing(
            10
        )

        # ----------------------------------------------------
        # Input controls
        # ----------------------------------------------------

        controls_group = QGroupBox(
            "IMAGE INPUT & ENCRYPTION CONTROLS"
        )

        controls = QVBoxLayout()

        row1 = QHBoxLayout()

        self.select_button = QPushButton(
            "Select Image"
        )

        self.select_button.clicked.connect(
            self.select_image
        )

        self.reset_button = QPushButton(
            "Clear / Reset"
        )

        self.reset_button.clicked.connect(
            self.clear_image
        )

        row1.addWidget(
            self.select_button
        )

        row1.addWidget(
            self.reset_button
        )

        row1.addStretch()

        controls.addLayout(
            row1
        )

        # ----------------------------------------------------
        # Metadata
        # ----------------------------------------------------

        metadata = QGridLayout()

        self.file_label = QLabel(
            "File: —"
        )

        self.dimensions_label = QLabel(
            "Dimensions: —"
        )

        self.mode_label = QLabel(
            "Mode: —"
        )

        metadata.addWidget(
            self.file_label,
            0,
            0
        )

        metadata.addWidget(
            self.dimensions_label,
            0,
            1
        )

        metadata.addWidget(
            self.mode_label,
            0,
            2
        )

        controls.addLayout(
            metadata
        )

        # ----------------------------------------------------
        # Key
        # ----------------------------------------------------

        key_row = QHBoxLayout()

        key_row.addWidget(
            QLabel("Encryption Key:")
        )

        self.key_input = QLineEdit()

        self.key_input.setPlaceholderText(
            "Enter encryption key"
        )

        self.key_input.setText(
            DEFAULT_KEY
        )

        self.key_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        key_row.addWidget(
            self.key_input
        )

        controls.addLayout(
            key_row
        )

        # ----------------------------------------------------
        # Buttons
        # ----------------------------------------------------

        button_row = QHBoxLayout()

        self.encrypt_button = QPushButton(
            "ENCRYPT IMAGE"
        )

        self.encrypt_button.setMinimumHeight(
            44
        )

        self.encrypt_button.setEnabled(
            False
        )

        self.encrypt_button.clicked.connect(
            self.encrypt_image
        )

        self.decrypt_button = QPushButton(
            "DECRYPT IMAGE"
        )

        self.decrypt_button.setMinimumHeight(
            44
        )

        self.decrypt_button.setEnabled(
            False
        )

        self.decrypt_button.clicked.connect(
            self.decrypt_image
        )

        self.analyze_button = QPushButton(
            "RUN SECURITY ANALYSIS"
        )

        self.analyze_button.setMinimumHeight(
            44
        )

        self.analyze_button.setEnabled(
            False
        )

        self.analyze_button.clicked.connect(
            self.run_security_analysis
        )

        button_row.addWidget(
            self.encrypt_button
        )

        button_row.addWidget(
            self.decrypt_button
        )

        button_row.addWidget(
            self.analyze_button
        )

        controls.addLayout(
            button_row
        )

        self.encrypt_button.setStyleSheet(f"""QPushButton {{ background-color: #075985; border: 1px solid {COLORS["cyan"]}; color: white; }} QPushButton:hover {{ background-color: #0E7490; }} QPushButton:pressed {{ background-color: #164E63; }} QPushButton:disabled {{ background-color: #101827; color: #526176; border-color: #1C2738; }}""")
        self.decrypt_button.setStyleSheet(f"""QPushButton {{ background-color: #4C1D95; border: 1px solid {COLORS["violet"]}; color: white; }} QPushButton:hover {{ background-color: #5B21B6; }} QPushButton:pressed {{ background-color: #3B0764; }} QPushButton:disabled {{ background-color: #101827; color: #526176; border-color: #1C2738; }}""")
        self.analyze_button.setStyleSheet(f"""QPushButton {{ background-color: #065F46; border: 1px solid {COLORS["green"]}; color: white; }} QPushButton:hover {{ background-color: #047857; }} QPushButton:pressed {{ background-color: #064E3B; }} QPushButton:disabled {{ background-color: #101827; color: #526176; border-color: #1C2738; }}""")

        controls_group.setLayout(
            controls
        )

        layout.addWidget(
            controls_group
        )

        # ----------------------------------------------------
        # Image pipeline
        # ----------------------------------------------------

        image_group = QGroupBox(
            "IMAGE PROCESSING PIPELINE"
        )

        image_layout = QGridLayout()

        image_layout.setSpacing(
            8
        )

        self.original_preview = ImagePreview(
            "Original image"
        )

        self.grayscale_preview = ImagePreview(
            "Grayscale image"
        )

        self.encrypted_preview = ImagePreview(
            "Encrypted image"
        )

        self.decrypted_preview = ImagePreview(
            "Decrypted image"
        )

        previews = [
            ("ORIGINAL", self.original_preview),
            ("GRAYSCALE", self.grayscale_preview),
            ("ENCRYPTED", self.encrypted_preview),
            ("DECRYPTED", self.decrypted_preview),
        ]

        for column, (title_text, preview) in enumerate(
            previews
        ):

            title_label = QLabel(
                title_text
            )

            title_label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            title_label.setStyleSheet(
                f"""QLabel {{ font-weight: 800; font-size: 11px; color: {COLORS["muted"]}; padding: 3px; }}"""
            )

            image_layout.addWidget(
                title_label,
                0,
                column
            )

            image_layout.addWidget(
                preview,
                1,
                column
            )

        image_group.setLayout(
            image_layout
        )

        layout.addWidget(
            image_group
        )

        # ----------------------------------------------------
        # Recovery verification
        # ----------------------------------------------------

        recovery_group = QGroupBox(
            "EXACT RECOVERY VERIFICATION"
        )

        recovery_layout = QGridLayout()

        self.recovery_status = QLabel(
            "Waiting for encryption and decryption..."
        )

        self.recovery_status.setWordWrap(
            True
        )

        self.maximum_difference_label = QLabel(
            "Maximum pixel difference: —"
        )

        self.total_difference_label = QLabel(
            "Total absolute difference: —"
        )

        recovery_layout.addWidget(
            self.recovery_status,
            0,
            0,
            1,
            2
        )

        recovery_layout.addWidget(
            self.maximum_difference_label,
            1,
            0
        )

        recovery_layout.addWidget(
            self.total_difference_label,
            1,
            1
        )

        recovery_group.setLayout(
            recovery_layout
        )

        layout.addWidget(
            recovery_group
        )

        # ----------------------------------------------------
        # Operation status
        # ----------------------------------------------------

        self.demo_operation_status = QLabel(
            "Select an image to begin."
        )

        self.demo_operation_status.setWordWrap(
            True
        )

        self.demo_operation_status.setStyleSheet(
            """
            QLabel {
                color: #8FA1B8;
                background-color: #0D1524;
                border: 1px solid #26344D;
                border-radius: 8px;
                padding: 9px;
            }
            """
        )

        layout.addWidget(
            self.demo_operation_status
        )

        layout.addStretch()

        widget.setLayout(
            layout
        )

        return widget

    # ========================================================
    # SECURITY TAB
    # ========================================================

    def create_security_tab(self):

        widget = QWidget()

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        container = QWidget()

        layout = QVBoxLayout()

        # ----------------------------------------------------
        # Run button
        # ----------------------------------------------------

        self.security_run_button = QPushButton(
            "RUN SECURITY ANALYSIS"
        )

        self.security_run_button.setMinimumHeight(
            42
        )

        self.security_run_button.setEnabled(
            False
        )

        self.security_run_button.clicked.connect(
            self.run_security_analysis
        )

        layout.addWidget(
            self.security_run_button
        )

        # ----------------------------------------------------
        # Security metric cards
        # ----------------------------------------------------

        metrics_group = QGroupBox(
            "SECURITY METRICS"
        )

        metrics_layout = QGridLayout()

        self.entropy_original_card = MetricCard(
            "ORIGINAL ENTROPY",
            "—",
            "Target for natural images varies."
        )

        self.entropy_encrypted_card = MetricCard(
            "ENCRYPTED ENTROPY",
            "—",
            "Ideal encrypted image approaches 8 bits."
        )

        self.horizontal_card = MetricCard(
            "HORIZONTAL CORRELATION",
            "—",
            "Ideal encrypted value approaches 0."
        )

        self.vertical_card = MetricCard(
            "VERTICAL CORRELATION",
            "—",
            "Ideal encrypted value approaches 0."
        )

        self.diagonal_card = MetricCard(
            "DIAGONAL CORRELATION",
            "—",
            "Ideal encrypted value approaches 0."
        )

        self.npcr_card = MetricCard(
            "NPCR",
            "—",
            "Measures percentage of changed pixels."
        )

        self.uaci_card = MetricCard(
            "UACI",
            "—",
            "Measures average intensity change."
        )

        self.uniformity_card = MetricCard(
            "HISTOGRAM UNIFORMITY",
            "—",
            "Lower normalized variance indicates greater uniformity."
        )

        cards = [
            self.entropy_original_card,
            self.entropy_encrypted_card,
            self.horizontal_card,
            self.vertical_card,
            self.diagonal_card,
            self.npcr_card,
            self.uaci_card,
            self.uniformity_card,
        ]

        for index, card in enumerate(cards):

            row = index // 4
            column = index % 4

            metrics_layout.addWidget(
                card,
                row,
                column
            )

        metrics_group.setLayout(
            metrics_layout
        )

        layout.addWidget(
            metrics_group
        )

        # ----------------------------------------------------
        # Key analysis
        # ----------------------------------------------------

        key_group = QGroupBox(
            "KEY ANALYSIS"
        )

        key_layout = QGridLayout()

        self.key_sensitivity_npcr = MetricCard(
            "KEY SENSITIVITY NPCR"
        )

        self.key_sensitivity_uaci = MetricCard(
            "KEY SENSITIVITY UACI"
        )

        self.key_space_card = MetricCard(
            "THEORETICAL KEY SPACE"
        )

        self.key_bits_card = MetricCard(
            "THEORETICAL KEY ENTROPY"
        )

        key_layout.addWidget(
            self.key_sensitivity_npcr,
            0,
            0
        )

        key_layout.addWidget(
            self.key_sensitivity_uaci,
            0,
            1
        )

        key_layout.addWidget(
            self.key_space_card,
            0,
            2
        )

        key_layout.addWidget(
            self.key_bits_card,
            0,
            3
        )

        key_group.setLayout(
            key_layout
        )

        layout.addWidget(
            key_group
        )

        # ----------------------------------------------------
        # Interpretation
        # ----------------------------------------------------

        interpretation_group = QGroupBox(
            "SECURITY INTERPRETATION"
        )

        interpretation_layout = QVBoxLayout()

        self.security_interpretation = QTextEdit()

        self.security_interpretation.setReadOnly(
            True
        )

        self.security_interpretation.setMinimumHeight(
            160
        )

        self.security_interpretation.setText(
            "Run the security analysis to generate an interpretation."
        )

        interpretation_layout.addWidget(
            self.security_interpretation
        )

        interpretation_group.setLayout(
            interpretation_layout
        )

        layout.addWidget(
            interpretation_group
        )

        layout.addStretch()

        container.setLayout(
            layout
        )

        scroll.setWidget(
            container
        )

        outer_layout = QVBoxLayout()

        outer_layout.addWidget(
            scroll
        )

        widget.setLayout(
            outer_layout
        )

        return widget

    # ========================================================
    # PERFORMANCE TAB
    # ========================================================

    def create_performance_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()

        # ----------------------------------------------------
        # Full encryption performance
        # ----------------------------------------------------

        full_group = QGroupBox(
            "FULL IMAGE ENCRYPTION PERFORMANCE"
        )

        full_layout = QGridLayout()

        self.encryption_time_card = MetricCard(
            "ENCRYPTION TIME"
        )

        self.decryption_time_card = MetricCard(
            "DECRYPTION TIME"
        )

        self.total_time_card = MetricCard(
            "TOTAL TIME"
        )

        self.performance_button = QPushButton(
            "RUN FULL PERFORMANCE TEST"
        )

        self.performance_button.setMinimumHeight(
            42
        )

        self.performance_button.setEnabled(
            self.original_array is not None
        )

        self.performance_button.clicked.connect(
            self.run_performance_test
        )

        layout.addWidget(
            self.performance_button
        )

        full_layout.addWidget(
            self.encryption_time_card,
            0,
            0
        )

        full_layout.addWidget(
            self.decryption_time_card,
            0,
            1
        )

        full_layout.addWidget(
            self.total_time_card,
            0,
            2
        )

        full_group.setLayout(
            full_layout
        )

        layout.addWidget(
            full_group
        )

        # ----------------------------------------------------
        # Quantum performance
        # ----------------------------------------------------

        quantum_group = QGroupBox(
            "QUANTUM KEYSTREAM PERFORMANCE"
        )

        quantum_layout = QVBoxLayout()

        self.quantum_table = QTableWidget(
            0,
            4
        )

        self.quantum_table.setHorizontalHeaderLabels(
            [
                "Requested Bits",
                "Generated Bits",
                "Time (s)",
                "Throughput (bits/s)"
            ]
        )

        self.quantum_table.horizontalHeader().setStretchLastSection(
            True
        )

        quantum_layout.addWidget(
            self.quantum_table
        )

        quantum_group.setLayout(
            quantum_layout
        )

        self.quantum_performance_button = QPushButton(
            "RUN QUANTUM KEYSTREAM TEST"
        )

        self.quantum_performance_button.clicked.connect(
            self.run_quantum_performance
        )

        layout.addWidget(
            self.quantum_performance_button
        )

        layout.addWidget(
            quantum_group
        )

        layout.addStretch()

        widget.setLayout(
            layout
        )

        return widget

    # ========================================================
    # NOISE TAB
    # ========================================================

    def create_noise_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()

        # ----------------------------------------------------
        # Explanation
        # ----------------------------------------------------

        info = QLabel(
            "This panel evaluates how simulated quantum noise "
            "changes the measurement distribution of the project "
            "circuit. Total Variation Distance (TVD) is used to "
            "compare ideal and noisy distributions."
        )

        info.setWordWrap(
            True
        )

        info.setStyleSheet(
            """
            QLabel {
                color: #999999;
                padding: 8px;
            }
            """
        )

        layout.addWidget(
            info
        )

        # ----------------------------------------------------
        # Noise buttons
        # ----------------------------------------------------

        button_row = QHBoxLayout()

        self.noise_button = QPushButton(
            "RUN NOISE ANALYSIS"
        )

        self.noise_button.setMinimumHeight(
            42
        )

        self.noise_button.clicked.connect(
            self.run_noise_analysis
        )

        button_row.addWidget(
            self.noise_button
        )

        layout.addLayout(
            button_row
        )

        # ----------------------------------------------------
        # Noise table
        # ----------------------------------------------------

        group = QGroupBox(
            "NOISE SWEEP"
        )

        group_layout = QVBoxLayout()

        self.noise_table = QTableWidget(
            0,
            3
        )

        self.noise_table.setHorizontalHeaderLabels(
            [
                "Noise Level",
                "TVD",
                "Interpretation"
            ]
        )

        self.noise_table.horizontalHeader().setStretchLastSection(
            True
        )

        group_layout.addWidget(
            self.noise_table
        )

        group.setLayout(
            group_layout
        )

        layout.addWidget(
            group
        )

        # ----------------------------------------------------
        # Noise explanation
        # ----------------------------------------------------

        self.noise_result_text = QTextEdit()

        self.noise_result_text.setReadOnly(
            True
        )

        self.noise_result_text.setMinimumHeight(
            180
        )

        self.noise_result_text.setText(
            "Run the noise analysis to populate this section."
        )

        layout.addWidget(
            self.noise_result_text
        )

        layout.addStretch()

        widget.setLayout(
            layout
        )

        return widget

    # ========================================================
    # ARCHITECTURE TAB
    # ========================================================

    def create_about_tab(self):

        widget = QWidget()

        scroll = QScrollArea()

        scroll.setWidgetResizable(
            True
        )

        container = QWidget()

        layout = QVBoxLayout()

        # ----------------------------------------------------
        # Project overview
        # ----------------------------------------------------

        overview = QGroupBox(
            "PROJECT OVERVIEW"
        )

        overview_layout = QVBoxLayout()

        overview_text = QLabel(
            """
<b>Quantum-Inspired Image Encryption Using Quantum Circuits</b>
<br><br>
This project implements a research-oriented image encryption
pipeline in which a quantum-circuit-based keystream generation
component is integrated with classical image permutation and
diffusion techniques.
<br><br>
The quantum component is simulated using Qiskit Aer.
The project is intended as an educational and experimental
prototype rather than a production cryptographic system.
"""
        )

        overview_text.setWordWrap(
            True
        )

        overview_layout.addWidget(
            overview_text
        )

        overview.setLayout(
            overview_layout
        )

        layout.addWidget(
            overview
        )

        # ----------------------------------------------------
        # Architecture
        # ----------------------------------------------------

        architecture = QGroupBox(
            "ENCRYPTION ARCHITECTURE"
        )

        architecture_layout = QVBoxLayout()

        architecture_text = QLabel(
            """
<b>1. INPUT IMAGE</b>
<br>
The selected image is loaded and converted to grayscale.
<br><br>

<b>2. KEY DERIVATION</b>
<br>
The user-provided encryption key is converted into deterministic
key material used by the encryption pipeline.
<br><br>

<b>3. BLOCK PERMUTATION</b>
<br>
The image is divided into 8×8 blocks and the blocks are
permuted according to key-derived material.
<br><br>

<b>4. LOCAL PIXEL PERMUTATION</b>
<br>
Pixels within individual blocks are rearranged.
<br><br>

<b>5. QUANTUM STREAM A</b>
<br>
A quantum-circuit-derived bitstream is generated and converted
into byte values.
<br><br>

<b>6. QUANTUM STREAM B</b>
<br>
A second quantum-derived stream is generated using a
domain-separated key.
<br><br>

<b>7. FORWARD DIFFUSION</b>
<br>
The first quantum stream participates in the forward diffusion
stage.
<br><br>

<b>8. BACKWARD DIFFUSION</b>
<br>
The second quantum stream participates in the backward
diffusion stage.
<br><br>

<b>9. ENCRYPTED IMAGE</b>
<br>
The transformed data is reconstructed into the encrypted image.
"""
        )

        architecture_text.setWordWrap(
            True
        )

        architecture_text.setStyleSheet(
            """
            QLabel {
                line-height: 1.5;
                padding: 8px;
            }
            """
        )

        architecture_layout.addWidget(
            architecture_text
        )

        architecture.setLayout(
            architecture_layout
        )

        layout.addWidget(
            architecture
        )

        # ----------------------------------------------------
        # Quantum circuit
        # ----------------------------------------------------

        quantum = QGroupBox(
            "QUANTUM CIRCUIT COMPONENT"
        )

        quantum_layout = QVBoxLayout()

        quantum_text = QLabel(
            """
The project's quantum keystream circuit contains:

• Hadamard gates for superposition
• CNOT gates for entanglement and mixing
• Key-derived rotation gates
• Measurement of the quantum register
• Qiskit Aer simulation

Conceptually:

        KEY
         │
         ▼
      SHA-256
         │
         ▼
   Rotation Angles
         │
         ▼
 ┌─────────────────┐
 │  H       H      │
 │  │       │      │
 │  CX      CX     │
 │  │       │      │
 │  RY      RZ     │
 │  │       │      │
 │  └───CX──┘      │
 │       │         │
 │   Measurement   │
 └───────┬─────────┘
         │
         ▼
   Quantum Bitstream
"""
        )

        quantum_text.setWordWrap(
            True
        )

        quantum_text.setStyleSheet(
            """
            QLabel {
                font-family: Consolas;
                color: #bbbbbb;
                padding: 10px;
            }
            """
        )

        quantum_layout.addWidget(
            quantum_text
        )

        quantum.setLayout(
            quantum_layout
        )

        layout.addWidget(
            quantum
        )

        # ----------------------------------------------------
        # Limitations
        # ----------------------------------------------------

        limitations = QGroupBox(
            "RESEARCH LIMITATIONS"
        )

        limitations_layout = QVBoxLayout()

        limitations_text = QLabel(
            """
• The quantum circuits are executed using simulation rather
  than physical quantum hardware.

• The quantum keystream implementation is a research prototype
  and should not be treated as a production cryptographic RNG.

• Security metrics such as entropy, correlation, NPCR and UACI
  provide experimental evidence but do not constitute a formal
  cryptographic security proof.

• Performance depends strongly on image size and simulator
  configuration.
"""
        )

        limitations_text.setWordWrap(
            True
        )

        limitations_layout.addWidget(
            limitations_text
        )

        limitations.setLayout(
            limitations_layout
        )

        layout.addWidget(
            limitations
        )

        layout.addStretch()

        container.setLayout(
            layout
        )

        scroll.setWidget(
            container
        )

        outer_layout = QVBoxLayout()

        outer_layout.addWidget(
            scroll
        )

        widget.setLayout(
            outer_layout
        )

        return widget

    # ========================================================
    # SELECT IMAGE
    # ========================================================

    def select_image(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.tif *.tiff)"
        )

        if not file_path:
            return

        try:

            image = load_image(
                file_path
            )

            if (
                image.width % 8 != 0
                or image.height % 8 != 0
            ):

                QMessageBox.warning(
                    self,
                    "Unsupported Image Size",
                    (
                        "Image dimensions must be divisible by 8.\n\n"
                        f"Current size: "
                        f"{image.width} × {image.height}"
                    )
                )

                return

            grayscale = convert_to_grayscale(
                image
            )

            grayscale_array = image_to_array(
                grayscale
            )

            self.selected_image_path = Path(
                file_path
            )

            self.original_image = image
            self.grayscale_image = grayscale

            self.original_array = np.asarray(
                grayscale_array,
                dtype=np.uint8
            )

            self.encrypted_array = None
            self.decrypted_array = None

            self.encrypted_image_path = None
            self.decrypted_image_path = None

            # ------------------------------------------------
            # Save grayscale
            # ------------------------------------------------

            RESULTS_DIR.mkdir(
                parents=True,
                exist_ok=True
            )

            grayscale.save(
                GUI_GRAYSCALE
            )

            # ------------------------------------------------
            # Display
            # ------------------------------------------------

            self.original_preview.set_image(
                file_path
            )

            self.grayscale_preview.set_image(
                GUI_GRAYSCALE
            )

            self.encrypted_preview.clear_image()
            self.decrypted_preview.clear_image()

            # ------------------------------------------------
            # Metadata
            # ------------------------------------------------

            self.file_label.setText(
                f"File: {self.selected_image_path.name}"
            )

            self.dimensions_label.setText(
                f"Dimensions: {image.width} × {image.height}"
            )

            self.mode_label.setText(
                f"Mode: {image.mode}"
            )

            # ------------------------------------------------
            # Controls
            # ------------------------------------------------

            self.encrypt_button.setEnabled(
                True
            )

            self.decrypt_button.setEnabled(
                False
            )

            self.analyze_button.setEnabled(
                False
            )

            self.security_run_button.setEnabled(
                False
            )

            self.performance_button.setEnabled(
                True
            )

            # ------------------------------------------------
            # Reset analysis
            # ------------------------------------------------

            self.reset_analysis_display()

            self.demo_operation_status.setText(
                "✓ Image loaded\n"
                "✓ Dimensions validated\n"
                "✓ Converted to grayscale\n"
                "✓ Ready for encryption"
            )

            self.set_status("● IMAGE READY")

            self.tabs.setCurrentIndex(
                0
            )

        except Exception as error:

            self.set_status("● ERROR")

            QMessageBox.critical(
                self,
                "Image Error",
                f"Unable to load image.\n\n{error}"
            )

    # ========================================================
    # ENCRYPT
    # ========================================================

    def encrypt_image(self):

        if self.original_array is None:

            QMessageBox.warning(
                self,
                "No Image",
                "Select an image first."
            )

            return

        key = self.key_input.text()

        if not key:

            QMessageBox.warning(
                self,
                "Missing Key",
                "Enter an encryption key."
            )

            return

        try:

            self.set_status("● ENCRYPTING...")

            self.demo_operation_status.setText(
                "⏳ Running encryption pipeline..."
            )

            self.encrypt_button.setEnabled(
                False
            )

            self.decrypt_button.setEnabled(
                False
            )

            QApplication.processEvents()

            start = time.perf_counter()

            encrypted = encrypt_array(
                self.original_array,
                key
            )

            elapsed = (
                time.perf_counter()
                - start
            )

            encrypted = np.asarray(
                encrypted,
                dtype=np.uint8
            )

            self.encrypted_array = encrypted

            encrypted_image = Image.fromarray(
                encrypted
            )

            encrypted_image.save(
                GUI_ENCRYPTED
            )

            self.encrypted_image_path = (
                GUI_ENCRYPTED
            )

            self.encrypted_preview.set_image(
                GUI_ENCRYPTED
            )

            self.encrypt_button.setEnabled(
                True
            )

            self.decrypt_button.setEnabled(
                True
            )

            self.analyze_button.setEnabled(
                True
            )

            self.security_run_button.setEnabled(
                True
            )

            self.performance_button.setEnabled(
                True
            )

            self.demo_operation_status.setText(
                "✓ Image loaded\n"
                "✓ Grayscale conversion completed\n"
                "✓ Quantum-derived encryption completed\n"
                f"✓ Encryption time: {elapsed:.4f} seconds\n"
                "→ Ready for decryption"
            )

            self.set_status("● ENCRYPTION COMPLETE")

        except Exception as error:

            self.encrypt_button.setEnabled(
                True
            )

            self.set_status("● ENCRYPTION ERROR")

            QMessageBox.critical(
                self,
                "Encryption Error",
                f"Encryption failed.\n\n{error}"
            )

    # ========================================================
    # DECRYPT
    # ========================================================

    def decrypt_image(self):

        if self.encrypted_array is None:

            QMessageBox.warning(
                self,
                "No Encrypted Image",
                "Encrypt the image first."
            )

            return

        key = self.key_input.text()

        if not key:

            QMessageBox.warning(
                self,
                "Missing Key",
                "Enter the encryption key."
            )

            return

        try:

            self.set_status("● DECRYPTING...")

            self.demo_operation_status.setText(
                "⏳ Running decryption pipeline..."
            )

            self.decrypt_button.setEnabled(
                False
            )

            QApplication.processEvents()

            start = time.perf_counter()

            decrypted = decrypt_array(
                self.encrypted_array,
                key
            )

            elapsed = (
                time.perf_counter()
                - start
            )

            decrypted = np.asarray(
                decrypted,
                dtype=np.uint8
            )

            self.decrypted_array = decrypted

            decrypted_image = Image.fromarray(
                decrypted
            )

            decrypted_image.save(
                GUI_DECRYPTED
            )

            self.decrypted_image_path = (
                GUI_DECRYPTED
            )

            self.decrypted_preview.set_image(
                GUI_DECRYPTED
            )

            # ------------------------------------------------
            # Exact recovery
            # ------------------------------------------------

            identical = np.array_equal(
                self.original_array,
                self.decrypted_array
            )

            difference = np.abs(
                self.original_array.astype(
                    np.int16
                )
                -
                self.decrypted_array.astype(
                    np.int16
                )
            )

            maximum_difference = int(
                np.max(difference)
            )

            total_difference = int(
                np.sum(difference)
            )

            if identical:

                self.recovery_status.setText(
                    "✓ EXACT RECOVERY VERIFIED\n"
                    "Decrypted image is identical to "
                    "the grayscale input."
                )

                self.recovery_status.setStyleSheet(
                    """
                    QLabel {
                        color: #55d66b;
                        font-weight: bold;
                        font-size: 14px;
                    }
                    """
                )

                self.set_status("● RECOVERY VERIFIED")

            else:

                self.recovery_status.setText(
                    "✗ EXACT RECOVERY FAILED"
                )

                self.recovery_status.setStyleSheet(
                    """
                    QLabel {
                        color: #ff5555;
                        font-weight: bold;
                        font-size: 14px;
                    }
                    """
                )

                self.set_status("● RECOVERY DIFFERENCE DETECTED")

            self.maximum_difference_label.setText(
                f"Maximum pixel difference: "
                f"{maximum_difference}"
            )

            self.total_difference_label.setText(
                f"Total absolute difference: "
                f"{total_difference}"
            )

            self.decrypt_button.setEnabled(
                True
            )

            self.demo_operation_status.setText(
                "✓ Image loaded\n"
                "✓ Grayscale conversion completed\n"
                "✓ Encryption completed\n"
                "✓ Decryption completed\n"
                f"✓ Decryption time: {elapsed:.4f} seconds\n"
                "✓ Recovery verification completed"
            )

        except Exception as error:

            self.decrypt_button.setEnabled(
                True
            )

            self.set_status("● DECRYPTION ERROR")

            QMessageBox.critical(
                self,
                "Decryption Error",
                f"Decryption failed.\n\n{error}"
            )

    # ========================================================
    # SECURITY ANALYSIS
    # ========================================================

    def run_security_analysis(self):

        if self.original_array is None:

            QMessageBox.warning(
                self,
                "No Image",
                "Select an image first."
            )

            return

        if self.encrypted_array is None:

            QMessageBox.warning(
                self,
                "No Encryption",
                "Encrypt the image first."
            )

            return

        key = self.key_input.text()

        if not key:

            QMessageBox.warning(
                self,
                "Missing Key",
                "Enter an encryption key."
            )

            return

        try:

            self.set_status("● ANALYZING SECURITY...")

            QApplication.processEvents()

            # ------------------------------------------------
            # Main metrics
            # ------------------------------------------------

            results = analyze_security(
                self.original_array,
                self.encrypted_array
            )

            original = results["original"]
            encrypted = results["encrypted"]

            # ------------------------------------------------
            # Differential
            # ------------------------------------------------

            key_sensitivity = (
                analyze_key_sensitivity(
                    self.original_array,
                    key
                )
            )

            key_space = (
                analyze_key_space(
                    key
                )
            )

            encrypted_histogram = (
                calculate_histogram(
                    self.encrypted_array
                )
            )

            uniformity = (
                histogram_uniformity_score(
                    encrypted_histogram
                )
            )

            # ------------------------------------------------
            # Store
            # ------------------------------------------------

            self.security_results = results
            self.key_sensitivity_results = (
                key_sensitivity
            )

            self.key_space_results = (
                key_space
            )

            # ------------------------------------------------
            # Display
            # ------------------------------------------------

            self.entropy_original_card.set_value(
                f"{original['entropy']:.6f}"
            )

            self.entropy_encrypted_card.set_value(
                f"{encrypted['entropy']:.6f}"
            )

            self.horizontal_card.set_value(
                f"{encrypted['horizontal_correlation']:.6f}"
            )

            self.vertical_card.set_value(
                f"{encrypted['vertical_correlation']:.6f}"
            )

            self.diagonal_card.set_value(
                f"{encrypted['diagonal_correlation']:.6f}"
            )

            self.npcr_card.set_value(
                f"{key_sensitivity['NPCR']:.6f}%"
            )

            self.uaci_card.set_value(
                f"{key_sensitivity['UACI']:.6f}%"
            )

            self.uniformity_card.set_value(
                f"{uniformity:.6f}"
            )

            self.key_sensitivity_npcr.set_value(
                f"{key_sensitivity['NPCR']:.6f}%"
            )

            self.key_sensitivity_uaci.set_value(
                f"{key_sensitivity['UACI']:.6f}%"
            )

            self.key_space_card.set_value(
                f"{key_space['key_space']:,}"
            )

            self.key_bits_card.set_value(
                f"{key_space['key_bits']:.2f} bits"
            )

            # ------------------------------------------------
            # Interpretation
            # ------------------------------------------------

            entropy_text = (
                "close to 8"
                if encrypted["entropy"] >= 7.9
                else "below 7.9"
            )

            correlation_values = [
                abs(
                    encrypted[
                        "horizontal_correlation"
                    ]
                ),
                abs(
                    encrypted[
                        "vertical_correlation"
                    ]
                ),
                abs(
                    encrypted[
                        "diagonal_correlation"
                    ]
                )
            ]

            low_correlation = all(
                value < 0.05
                for value in correlation_values
            )

            interpretation = (
                f"Encrypted-image entropy is "
                f"{encrypted['entropy']:.6f}, which is "
                f"{entropy_text}.\n\n"
            )

            interpretation += (
                "Encrypted adjacent-pixel correlations "
                f"are {'close to zero' if low_correlation else 'not all close to zero'}.\n\n"
            )

            interpretation += (
                f"Key-sensitivity NPCR: "
                f"{key_sensitivity['NPCR']:.6f}%.\n"
                f"Key-sensitivity UACI: "
                f"{key_sensitivity['UACI']:.6f}%.\n\n"
            )

            interpretation += (
                f"Theoretical key-space entropy for the "
                f"supplied key length is "
                f"{key_space['key_bits']:.2f} bits."
            )

            self.security_interpretation.setText(
                interpretation
            )

            self.set_status("● SECURITY ANALYSIS COMPLETE")

            self.tabs.setCurrentIndex(
                1
            )

        except Exception as error:

            self.set_status("● ANALYSIS ERROR")

            QMessageBox.critical(
                self,
                "Security Analysis Error",
                f"Security analysis failed.\n\n{error}"
            )

    # ========================================================
    # PERFORMANCE TEST
    # ========================================================

    def run_performance_test(self):

        if self.original_array is None:

            QMessageBox.warning(
                self,
                "No Image",
                "Select an image first."
            )

            return

        key = self.key_input.text()

        if not key:

            QMessageBox.warning(
                self,
                "Missing Key",
                "Enter an encryption key."
            )

            return

        try:

            self.set_status("● RUNNING PERFORMANCE TEST...")

            QApplication.processEvents()

            # ------------------------------------------------
            # Encryption
            # ------------------------------------------------

            start = time.perf_counter()

            encrypted = encrypt_array(
                self.original_array,
                key
            )

            encryption_time = (
                time.perf_counter()
                - start
            )

            # ------------------------------------------------
            # Decryption
            # ------------------------------------------------

            start = time.perf_counter()

            decrypted = decrypt_array(
                encrypted,
                key
            )

            decryption_time = (
                time.perf_counter()
                - start
            )

            total_time = (
                encryption_time
                + decryption_time
            )

            self.performance_results = {
                "encryption":
                    encryption_time,
                "decryption":
                    decryption_time,
                "total":
                    total_time
            }

            self.encryption_time_card.set_value(
                f"{encryption_time:.4f} s"
            )

            self.decryption_time_card.set_value(
                f"{decryption_time:.4f} s"
            )

            self.total_time_card.set_value(
                f"{total_time:.4f} s"
            )

            self.set_status("● PERFORMANCE TEST COMPLETE")

        except Exception as error:

            self.set_status("● PERFORMANCE ERROR")

            QMessageBox.critical(
                self,
                "Performance Error",
                f"Performance test failed.\n\n{error}"
            )

    # ========================================================
    # QUANTUM PERFORMANCE
    # ========================================================

    def run_quantum_performance(self):

        key = self.key_input.text()

        if not key:

            key = DEFAULT_KEY

        bit_sizes = [
            128,
            512,
            1024,
            4096,
            8192
        ]

        try:

            self.set_status("● TESTING QUANTUM KEYSTREAM...")

            QApplication.processEvents()

            self.quantum_table.setRowCount(
                0
            )

            results = []

            for number_of_bits in bit_sizes:

                start = time.perf_counter()

                bits = generate_quantum_bits(
                    key,
                    number_of_bits
                )

                elapsed = (
                    time.perf_counter()
                    - start
                )

                throughput = (
                    number_of_bits / elapsed
                    if elapsed > 0
                    else 0
                )

                results.append(
                    (
                        number_of_bits,
                        len(bits),
                        elapsed,
                        throughput
                    )
                )

                row = (
                    self.quantum_table.rowCount()
                )

                self.quantum_table.insertRow(
                    row
                )

                values = [
                    str(number_of_bits),
                    str(len(bits)),
                    f"{elapsed:.6f}",
                    f"{throughput:.2f}"
                ]

                for column, value in enumerate(
                    values
                ):

                    self.quantum_table.setItem(
                        row,
                        column,
                        QTableWidgetItem(value)
                    )

                QApplication.processEvents()

            self.quantum_performance_results = (
                results
            )

            self.set_status("● QUANTUM PERFORMANCE COMPLETE")

        except Exception as error:

            self.set_status("● QUANTUM PERFORMANCE ERROR")

            QMessageBox.critical(
                self,
                "Quantum Performance Error",
                f"Quantum performance test failed.\n\n{error}"
            )

    # ========================================================
    # NOISE ANALYSIS
    # ========================================================

    def run_noise_analysis(self):

        try:

            from qiskit import QuantumCircuit
            from qiskit_aer import AerSimulator

            from src.noise.noise_models import (
                create_depolarizing_noise_model,
                create_readout_noise_model,
            )

            self.set_status("● RUNNING QUANTUM NOISE ANALYSIS...")

            QApplication.processEvents()

            # ------------------------------------------------
            # Circuit
            # ------------------------------------------------

            circuit = QuantumCircuit(
                4,
                4
            )

            circuit.h(0)
            circuit.h(1)

            circuit.cx(0, 2)
            circuit.cx(1, 3)

            circuit.ry(
                0.5,
                0
            )

            circuit.rz(
                1.0,
                1
            )

            circuit.cx(
                2,
                3
            )

            circuit.measure(
                [0, 1, 2, 3],
                [0, 1, 2, 3]
            )

            shots = 1000
            seed = 12345

            # ------------------------------------------------
            # Ideal
            # ------------------------------------------------

            ideal_simulator = AerSimulator(
                seed_simulator=seed
            )

            ideal_result = (
                ideal_simulator
                .run(
                    circuit,
                    shots=shots
                )
                .result()
            )

            ideal_counts = (
                ideal_result.get_counts()
            )

            # ------------------------------------------------
            # Noise sweep
            # ------------------------------------------------

            noise_levels = [
                0.001,
                0.005,
                0.01,
                0.02,
                0.05
            ]

            self.noise_table.setRowCount(
                0
            )

            results = []

            for error_rate in noise_levels:

                noise_model = (
                    create_depolarizing_noise_model(
                        single_qubit_error=error_rate,
                        two_qubit_error=error_rate
                    )
                )

                simulator = AerSimulator(
                    noise_model=noise_model,
                    seed_simulator=seed
                )

                result = (
                    simulator
                    .run(
                        circuit,
                        shots=shots
                    )
                    .result()
                )

                noisy_counts = (
                    result.get_counts()
                )

                tvd = (
                    total_variation_distance(
                        ideal_counts,
                        noisy_counts
                    )
                )

                results.append(
                    (
                        error_rate,
                        tvd
                    )
                )

                row = (
                    self.noise_table.rowCount()
                )

                self.noise_table.insertRow(
                    row
                )

                if tvd < 0.05:

                    interpretation = (
                        "Low distribution change"
                    )

                elif tvd < 0.15:

                    interpretation = (
                        "Moderate distribution change"
                    )

                else:

                    interpretation = (
                        "Significant distribution change"
                    )

                values = [
                    f"{error_rate:.3f}",
                    f"{tvd:.6f}",
                    interpretation
                ]

                for column, value in enumerate(
                    values
                ):

                    self.noise_table.setItem(
                        row,
                        column,
                        QTableWidgetItem(value)
                    )

                QApplication.processEvents()

            # ------------------------------------------------
            # Readout example
            # ------------------------------------------------

            readout_model = (
                create_readout_noise_model(
                    probability_0_to_1=0.01,
                    probability_1_to_0=0.01
                )
            )

            readout_simulator = AerSimulator(
                noise_model=readout_model,
                seed_simulator=seed
            )

            readout_result = (
                readout_simulator
                .run(
                    circuit,
                    shots=shots
                )
                .result()
            )

            readout_counts = (
                readout_result.get_counts()
            )

            readout_tvd = (
                total_variation_distance(
                    ideal_counts,
                    readout_counts
                )
            )

            self.noise_results = {
                "depolarizing":
                    results,
                "readout_tvd":
                    readout_tvd
            }

            text = (
                "QUANTUM NOISE ANALYSIS\n"
                "======================\n\n"
                f"Shots: {shots}\n\n"
                "The ideal circuit distribution was used "
                "as the reference distribution.\n\n"
            )

            for error_rate, tvd in results:

                text += (
                    f"Depolarizing error "
                    f"{error_rate:.3f}: "
                    f"TVD = {tvd:.6f}\n"
                )

            text += (
                "\nReadout-noise example:\n"
                f"TVD = {readout_tvd:.6f}\n\n"
                "Interpretation:\n"
                "Increasing simulated noise generally "
                "increases the difference between the "
                "ideal and noisy measurement distributions."
            )

            self.noise_result_text.setText(
                text
            )

            self.set_status("● QUANTUM NOISE ANALYSIS COMPLETE")

        except Exception as error:

            self.set_status("● NOISE ANALYSIS ERROR")

            QMessageBox.critical(
                self,
                "Noise Analysis Error",
                f"Noise analysis failed.\n\n{error}"
            )

    # ========================================================
    # RESET ANALYSIS
    # ========================================================

    def reset_analysis_display(self):

        cards = [
            self.entropy_original_card,
            self.entropy_encrypted_card,
            self.horizontal_card,
            self.vertical_card,
            self.diagonal_card,
            self.npcr_card,
            self.uaci_card,
            self.uniformity_card,
            self.key_sensitivity_npcr,
            self.key_sensitivity_uaci,
            self.key_space_card,
            self.key_bits_card,
            self.encryption_time_card,
            self.decryption_time_card,
            self.total_time_card,
        ]

        for card in cards:

            card.set_value(
                "—"
            )

        self.quantum_table.setRowCount(
            0
        )

        self.noise_table.setRowCount(
            0
        )

        self.security_interpretation.setText(
            "Run the security analysis to generate an interpretation."
        )

        self.noise_result_text.setText(
            "Run the noise analysis to populate this section."
        )

        self.recovery_status.setText(
            "Waiting for encryption and decryption..."
        )

        self.recovery_status.setStyleSheet(
            ""
        )

        self.maximum_difference_label.setText(
            "Maximum pixel difference: —"
        )

        self.total_difference_label.setText(
            "Total absolute difference: —"
        )

    # ========================================================
    # CLEAR / RESET
    # ========================================================

    def clear_image(self):

        self.selected_image_path = None

        self.original_image = None
        self.grayscale_image = None

        self.original_array = None
        self.encrypted_array = None
        self.decrypted_array = None

        self.encrypted_image_path = None
        self.decrypted_image_path = None

        self.original_preview.clear_image()
        self.grayscale_preview.clear_image()
        self.encrypted_preview.clear_image()
        self.decrypted_preview.clear_image()

        self.key_input.setText(
            DEFAULT_KEY
        )

        self.file_label.setText(
            "File: —"
        )

        self.dimensions_label.setText(
            "Dimensions: —"
        )

        self.mode_label.setText(
            "Mode: —"
        )

        self.encrypt_button.setEnabled(
            False
        )

        self.decrypt_button.setEnabled(
            False
        )

        self.analyze_button.setEnabled(
            False
        )

        self.security_run_button.setEnabled(
            False
        )

        self.performance_button.setEnabled(
            False
        )

        self.reset_analysis_display()

        self.demo_operation_status.setText(
            "Select an image to begin."
        )

        self.set_status("● READY")

        self.tabs.setCurrentIndex(
            0
        )


# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

def run_gui():

    app = QApplication(
        sys.argv
    )

    # --------------------------------------------------------
    # Font
    # --------------------------------------------------------

    font = QFont()

    font.setPointSize(
        10
    )

    app.setFont(
        font
    )

    # --------------------------------------------------------
    # Dark professional theme
    # --------------------------------------------------------

    app.setStyleSheet(
        """
        QMainWindow {
            background-color: #101010;
        }

        QWidget {
            background-color: #101010;
            color: #eeeeee;
        }

        QTabWidget::pane {
            border: 1px solid #353535;
            border-radius: 8px;
            background-color: #101010;
        }

        QTabBar::tab {
            background-color: #181818;
            color: #999999;
            border: 1px solid #303030;
            padding: 9px 18px;
            margin-right: 2px;
        }

        QTabBar::tab:selected {
            background-color: #292929;
            color: #ffffff;
        }

        QGroupBox {
            border: 1px solid #353535;
            border-radius: 9px;
            margin-top: 12px;
            padding: 12px;
            font-weight: bold;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            left: 12px;
            padding: 0 7px;
            color: #cccccc;
        }

        QPushButton {
            background-color: #252525;
            border: 1px solid #444444;
            border-radius: 7px;
            padding: 8px 16px;
            color: #eeeeee;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #333333;
        }

        QPushButton:pressed {
            background-color: #414141;
        }

        QPushButton:disabled {
            background-color: #181818;
            color: #666666;
            border-color: #292929;
        }

        QLineEdit {
            background-color: #181818;
            border: 1px solid #444444;
            border-radius: 7px;
            padding: 9px;
            color: #eeeeee;
        }

        QLineEdit:focus {
            border: 1px solid #777777;
        }

        QTableWidget {
            background-color: #171717;
            alternate-background-color: #1d1d1d;
            gridline-color: #333333;
            border: 1px solid #353535;
        }

        QHeaderView::section {
            background-color: #252525;
            color: #dddddd;
            padding: 7px;
            border: 1px solid #353535;
        }

        QScrollArea {
            border: none;
        }

        QTextEdit {
            background-color: #171717;
            border: 1px solid #353535;
            border-radius: 7px;
            color: #cccccc;
            padding: 8px;
        }

        QProgressBar {
            background-color: #181818;
            border: 1px solid #333333;
            border-radius: 5px;
        }

        QLabel {
            color: #eeeeee;
        }
        """
    )

    window = QuantumImageEncryptionGUI()

    window.show()

    return app.exec()


if __name__ == "__main__":

    run_gui()