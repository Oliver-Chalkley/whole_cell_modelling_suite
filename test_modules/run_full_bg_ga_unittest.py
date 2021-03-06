import sys
sys.path.insert(0, '/space/oc13378/myprojects/github/published_libraries/whole_cell_modelling_suite')
sys.path.insert(0, '/space/oc13378/myprojects/github/published_libraries/computer_communication_framework')
import whole_cell_modelling_suite.connections as connections
import whole_cell_modelling_suite.job_management as job_management
import whole_cell_modelling_suite.genetic_algorithms as genetic_algorithms
import pathlib
from statistics import mean

# CONNECTION DETAILS

# USER DETAILS STUFF
username = 'oc13378'
conn_alias = 'bg'
forename = 'Oliver'
surname = 'Chalkley'
email = 'oc13378@bristol.ac.uk'
affiliation = 'Unittest'

# PATH STUFF
relative_base_that_gets_deleted = 'wcms'
base_path_on_cluster = '/projects/flex1/database/wcm_suite/unittest'
output_path = 'output'
full_output_path = base_path_on_cluster + '/' + relative_base_that_gets_deleted + '/' + output_path
runfiles_path = 'runfiles'
full_runfiles_path = base_path_on_cluster + '/' + relative_base_that_gets_deleted + '/' + runfiles_path
wholecell_model_master = '/projects/flex1/database/wcm_suite/unittest/unittest-master'

bg_conn = connections.Karr2012Bg(username, conn_alias, forename, surname, email, full_output_path, full_runfiles_path, wholecell_model_master, affiliation = affiliation)

out_and_error_files = 'out_and_error_files'
full_out_and_error_files = base_path_on_cluster + '/' + relative_base_that_gets_deleted + '/' + out_and_error_files

master_dir = '/projects/flex1/database/wcm_suite/unittest/unittest-master'
createDataDictForSpecialistFunctionsFunctionNameUT = 'createDataDictForUnittest'
createSubmissionScriptFunctionNameUT = 'createUnittestScript'
createDictOfFileSourceToFileDestinationsFunctionNameUT = 'createDictOfFileSourceToFileDestinationForUnittest'
createAllFilesFunctionNameUT = 'createAllFilesForUnittest'
getDataForDbFunctionName = 'getGrowthAndDivisionTime'

# INPUT PARAMETERS
standard_generation_no_to_pop_size_dict =  {0: 5, 1: 2, -1: 1}

standard_random_kos_params_dict = {'populationSize_params_dict': standard_generation_no_to_pop_size_dict, 'getPopulationSizeFuncName': 'getPopulationSizeFromDict', 'getGeneCodeToIdDictFuncName': 'getGeneCodeToIdDictStandard', 'geneCodeToId_params_dict': None, 'min_ko_set_size': 2, 'max_ko_set_size': 5}

standardGetNewGeneration_params_dict = {'generationZeroFuncName': 'getRandomKos', 'genZero_params_dict': standard_random_kos_params_dict, 'noSurvivorsFuncName': 'getRandomKos', 'noSurvivors_params_dict': standard_random_kos_params_dict, 'minPopulationFuncName': 'getRandomKos', 'minPopulation_params_dict': standard_random_kos_params_dict, 'hasNoLengthFuncName': 'getRandomKos', 'noLength_params_dict': standard_random_kos_params_dict, 'min_population_to_start_mating': 4, 'mate_the_fittest_dict': {'getFittestProbabilitiesFuncName': 'getLinearProbsForMaximising', 'fittestProbabilities_params_dict': None, 'populationSize_params_dict': standard_generation_no_to_pop_size_dict, 'getPopulationSizeFuncName': 'getPopulationSizeFromDict', 'mateTwoParentsFuncName': 'mixMate', 'mateTwoParents_params_dict': None, 'mutateChildFuncName': 'exponentialMutation', 'mutateChild_params_dict': {'mutation_probability': 0.4, 'exponential_parameter': 2}}}

createJobSubmisions_params_dict = {'createAllFilesFuncName': createAllFilesFunctionNameUT, 'createDataDictForSpecialistFunctionsFunctionName': createDataDictForSpecialistFunctionsFunctionNameUT, 'createSubmissionScriptFunctionName': createSubmissionScriptFunctionNameUT, 'createDictOfFileSourceToFileDestinationsFunctionName': createDictOfFileSourceToFileDestinationsFunctionNameUT, 'first_wait_time': 10, 'second_wait_time': 7}

# CREATE GA INSTANCE
ga_inst = genetic_algorithms.Karr2012GeneticAlgorithmGeneKo({'bg': bg_conn}, 'bg_ga_proper_scoring_oc2', 'unittest_sim_output', 3, 'stopAtMaxGeneration', {'max_generation': 10}, 'standardGetNewGeneration', standardGetNewGeneration_params_dict, 'standardRunSimulations', {'createJobSubmissionFuncName': 'standardKoSubmissionFunction', 'createJobSubmisions_params_dict': createJobSubmisions_params_dict}, 4, genetic_algorithms.Karr2012MgaBase.getGeneCodesToIdDict(bg_conn, genetic_algorithms.Karr2012MgaBase.getJr358Genes()), '/space/oc13378/myprojects/github/published_libraries/whole-cell-modelling-suite/whole-cell-modelling-suite/temp_storage', 'max', 'aliveAndSmallestGenome', {'overallScoreFuncName': 'overallScoreBasic', 'rawScoreFunc': mean})
ga_inst.run()
