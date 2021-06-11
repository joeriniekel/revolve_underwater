#!/usr/bin/env python3
from pyrevolve import parser
from pyrevolve.evolution import fitness
from pyrevolve.evolution.selection import multiple_selection, tournament_selection
from pyrevolve.evolution.population import Population, PopulationConfig
from pyrevolve.evolution.pop_management.steady_state import steady_state_population_management
from pyrevolve.experiment_management import ExperimentManagement
from pyrevolve.genotype.plasticoding.crossover.crossover import CrossoverConfig
from pyrevolve.genotype.plasticoding.crossover.standard_crossover import standard_crossover
from pyrevolve.genotype.plasticoding.initialization import random_initialization
from pyrevolve.genotype.plasticoding.mutation.mutation import MutationConfig
from pyrevolve.genotype.plasticoding.mutation.standard_mutation import standard_mutation
from pyrevolve.genotype.plasticoding.plasticoding import PlasticodingConfig


async def run():

    # Define the size
    population_size = 20
    offspring_size = 10

    # Define the maximum number of structural modules per robot
    genotype_conf = PlasticodingConfig(
        max_structural_modules=100
    )
    # Define the mutation probability
    mutation_conf = MutationConfig(
        mutation_prob=0.8,
        genotype_conf=genotype_conf,
    )
    # Define the Crossover probability
    crossover_conf = CrossoverConfig(
        crossover_prob=0.8,
    )

    # Parse command line / file input arguments
    settings = parser.parse_args()
    experiment_management = ExperimentManagement(settings)

    # Insert the population parameters PopulationConfig:
    #   Creates a PopulationConfig object that sets the particular configuration for the population
    #
    #         :param population_size: size of the population
    #         :param genotype_constructor: class of the genotype used
    #         :param genotype_conf: configuration for genotype constructor
    #         :param fitness_function: function that takes in a `RobotManager` as a parameter and produces a fitness for the robot
    #         :param mutation_operator: operator to be used in mutation
    #         :param mutation_conf: configuration for mutation operator
    #         :param crossover_operator: operator to be used in crossover
    #         :param selection: selection type
    #         :param parent_selection: selection type during parent selection
    #         :param population_management: type of population management ie. steady state or generational
    #         :param evaluation_time: duration of an experiment
    #         :param experiment_name: name for the folder of the current experiment
    #         :param experiment_management: object with methods for managing the current experiment
    #         :param offspring_size (optional): size of offspring (for steady state)
    population_conf = PopulationConfig(
        population_size=population_size,
        genotype_constructor=random_initialization,
        genotype_conf=genotype_conf,
        fitness_function=fitness.displacement_velocity,
        mutation_operator=standard_mutation,
        mutation_conf=mutation_conf,
        crossover_operator=standard_crossover,
        crossover_conf=crossover_conf,
        selection=lambda individuals: tournament_selection(individuals, 2),
        parent_selection=lambda individuals: multiple_selection(individuals, 2, tournament_selection),
        population_management=steady_state_population_management,
        population_management_selector=tournament_selection,
        evaluation_time=settings.evaluation_time,
        offspring_size=offspring_size,
        experiment_name=settings.experiment_name,
        experiment_management=experiment_management
    )