monte_carlo.mc_master.active = True
monte_carlo.mc_master.generate_dispersions = False

exec(open('RUN_ERROR_IO_error2/input.py').read())
monte_carlo.mc_master.monte_run_number = 0

monte_carlo.x_file_lookup[0] = 2
