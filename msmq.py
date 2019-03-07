import winstats
import requests
import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name

# Please replace <hostname> and <queuename> with the relevant values

class MsmqPlugin(BasePlugin):
    def query(self, **kwargs):

        pgi = self.find_single_process_group(pgi_name('Windows System'))
        pgi_id = pgi.group_instance_id

        queue1 = winstats.get_perf_data(r'\MSMQ Queue(<hostname>\private$\<queuename>)\Messages in Queue', fmts='double', delay=100)
        queue2 = winstats.get_perf_data(r'\MSMQ Queue(<hostname>\private$\<queuename>)\Messages in Queue', fmts='double', delay=100)

        self.results_builder.relative(key='<queuename>', value=<queuename>[0], entity_id=pgi_id)
        self.results_builder.relative(key='<queuename>', value=<queuename>[0], entity_id=pgi_id)
