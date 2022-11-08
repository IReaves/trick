#!/usr/bin/env python3
import os, sys

sys.path.append(os.path.abspath("../../../share/trick/trickops/"))

from TrickWorkflow import *
class ExampleWorkflow(TrickWorkflow):
    def __init__( self, quiet, trick_top_level=os.path.abspath("../../../")):
        # Base Class initialize, this creates internal management structures
        TrickWorkflow.__init__(self, project_top_level=trick_top_level, log_dir='test/SIM_mc_generation/MCGTrickOps/TrickOpsLogs/', trick_dir=trick_top_level, config_file="test/SIM_mc_generation/MCGTrickOps/MCGenerationTest.yml", cpus=3, quiet=quiet)
    def run( self):
      build_jobs      = self.get_jobs(kind='build')
      run_jobs        = self.get_jobs(kind='run')
      ret = self.compare()
      builds_status = self.execute_jobs(build_jobs, max_concurrent=3, header='Executing all sim builds.')
      runs_status   = self.execute_jobs(run_jobs,   max_concurrent=3, header='Executing all sim runs.')
      self.report()           # Print Verbose report
      self.status_summary()   # Print a Succinct summary
      return (builds_status or runs_status or self.config_errors)
if __name__ == "__main__":
      ExampleWorkflow(quiet=True).run()
