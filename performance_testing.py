import pstats
# Load the profiling results
stats = pstats.Stats('profile_results.txt')

# Print the profiling statistics
stats.strip_dirs().sort_stats(-1).print_stats()
