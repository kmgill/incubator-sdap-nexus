
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
ARG tag_version=latest
FROM sdap/solr:${tag_version}
MAINTAINER Apache SDAP "dev@sdap.apache.org"

USER root

COPY create-core.sh /docker-entrypoint-initdb.d/create-core.sh
RUN echo "${SOLR_USER} ALL=(ALL) NOPASSWD: /usr/bin/cp -r /tmp/nexustiles/* ${SOLR_HOME}/nexustiles/" >> /etc/sudoers && \
  echo "${SOLR_USER} ALL=(ALL) NOPASSWD: /usr/bin/chown -R ${SOLR_USER}\:${SOLR_GROUP} ${SOLR_HOME}/nexustiles" >> /etc/sudoers

USER ${SOLR_USER}
VOLUME ${SOLR_HOME}/nexustiles

ENTRYPOINT ["solr-foreground"]
