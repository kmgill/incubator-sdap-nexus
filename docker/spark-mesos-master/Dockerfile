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

ARG tag_version=1.0.0-SNAPSHOT
FROM sdap/spark-mesos-base:${tag_version}

MAINTAINER Apache SDAP "dev@sdap.apache.org"

EXPOSE ${MESOS_MASTER_PORT}

# Run a Mesos master.

WORKDIR ${MESOS_HOME}/build

CMD ["/bin/bash", "-c", "./bin/mesos-master.sh --ip=${MESOS_IP} --hostname=${MESOS_MASTER_NAME} --port=${MESOS_MASTER_PORT} --work_dir=${MESOS_WORKDIR}"]
