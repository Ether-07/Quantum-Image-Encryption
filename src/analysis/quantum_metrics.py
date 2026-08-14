import numpy as np


def counts_to_probability(
    counts
):
    """
    Convert measurement counts into
    a probability distribution.
    """

    total = sum(
        counts.values()
    )

    if total == 0:
        return {}

    return {
        state: count / total
        for state, count in counts.items()
    }


def total_variation_distance(
    counts_a,
    counts_b
):
    """
    Calculate total variation distance
    between two discrete distributions.

    Range:
        0 -> identical distributions
        1 -> maximally separated
    """

    probabilities_a = (
        counts_to_probability(
            counts_a
        )
    )

    probabilities_b = (
        counts_to_probability(
            counts_b
        )
    )


    states = (
        set(probabilities_a)
        |
        set(probabilities_b)
    )


    distance = 0.0


    for state in states:

        probability_a = (
            probabilities_a
            .get(
                state,
                0.0
            )
        )

        probability_b = (
            probabilities_b
            .get(
                state,
                0.0
            )
        )


        distance += abs(
            probability_a
            - probability_b
        )


    return 0.5 * distance