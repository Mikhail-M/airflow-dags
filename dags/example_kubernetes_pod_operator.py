#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example Airflow DAG for Google Kubernetes Engine.
"""

import os

from airflow import models
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
Variable

GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "fifth-repeater-110906")
GCP_LOCATION = os.environ.get("GCP_GKE_LOCATION", "us-central1-c")
CLUSTER_NAME = os.environ.get("GCP_GKE_CLUSTER_NAME", "cluster-1")
    

with models.DAG(
    "example_gcp_gke",
    schedule_interval=None,  # Override to match your needs
    start_date=days_ago(1),
    tags=['example'],
) as dag:

    kubernetes_min_pod = KubernetesPodOperator(
        # The ID specified for the task.
        task_id='pod-ex-minimum',
        # Name of task you want to run, used to generate Pod ID.
        name='pod-ex-minimum',
        cmds=['echo', "kek"],
        namespace=,
        service_account_name="airflow-scheduler",
        image='alpine')

