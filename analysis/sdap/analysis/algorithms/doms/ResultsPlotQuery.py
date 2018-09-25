# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import BaseDomsHandler
import histogramplot
import mapplot
import scatterplot
from sdap.analysis.NexusHandler import nexus_handler


class PlotTypes:
    SCATTER = "scatter"
    MAP = "map"
    HISTOGRAM = "histogram"


@nexus_handler
class DomsResultsPlotHandler(BaseDomsHandler.BaseDomsQueryHandler):
    name = "DOMS Results Plotting"
    path = "/domsplot"
    description = ""
    params = {}
    singleton = True

    def __init__(self):
        BaseDomsHandler.BaseDomsQueryHandler.__init__(self)

    def calc(self, computeOptions, **args):
        id = computeOptions.get_argument("id", None)
        parameter = computeOptions.get_argument('parameter', 'sst')

        plotType = computeOptions.get_argument("type", PlotTypes.SCATTER)

        normAndCurve = computeOptions.get_boolean_arg("normandcurve", False)

        if plotType == PlotTypes.SCATTER:
            return scatterplot.createScatterPlot(id, parameter)
        elif plotType == PlotTypes.MAP:
            return mapplot.createMapPlot(id, parameter)
        elif plotType == PlotTypes.HISTOGRAM:
            return histogramplot.createHistogramPlot(id, parameter, normAndCurve)
        else:
            raise Exception("Unsupported plot type '%s' specified." % plotType)
