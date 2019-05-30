# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerProbe(Model):
    """The container probe, for liveness or readiness.

    :param exec_property: The execution command to probe
    :type exec_property: ~azure.mgmt.containerinstance.models.ContainerExec
    :param http_get: The Http Get settings to probe
    :type http_get: ~azure.mgmt.containerinstance.models.ContainerHttpGet
    :param initial_delay_seconds: The initial delay seconds.
    :type initial_delay_seconds: int
    :param period_seconds: The period seconds.
    :type period_seconds: int
    :param failure_threshold: The failure threshold.
    :type failure_threshold: int
    :param success_threshold: The success threshold.
    :type success_threshold: int
    :param timeout_seconds: The timeout seconds.
    :type timeout_seconds: int
    """

    _attribute_map = {
        'exec_property': {'key': 'exec', 'type': 'ContainerExec'},
        'http_get': {'key': 'httpGet', 'type': 'ContainerHttpGet'},
        'initial_delay_seconds': {'key': 'initialDelaySeconds', 'type': 'int'},
        'period_seconds': {'key': 'periodSeconds', 'type': 'int'},
        'failure_threshold': {'key': 'failureThreshold', 'type': 'int'},
        'success_threshold': {'key': 'successThreshold', 'type': 'int'},
        'timeout_seconds': {'key': 'timeoutSeconds', 'type': 'int'},
    }

    def __init__(self, *, exec_property=None, http_get=None, initial_delay_seconds: int=None, period_seconds: int=None, failure_threshold: int=None, success_threshold: int=None, timeout_seconds: int=None, **kwargs) -> None:
        super(ContainerProbe, self).__init__(**kwargs)
        self.exec_property = exec_property
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.failure_threshold = failure_threshold
        self.success_threshold = success_threshold
        self.timeout_seconds = timeout_seconds