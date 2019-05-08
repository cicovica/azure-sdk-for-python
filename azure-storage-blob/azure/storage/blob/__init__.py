# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

__version__ = "2.0.0a1"

from .common import BlobType
from .blob_service_client import BlobServiceClient
from .container_client import ContainerClient
from .blob_client import BlobClient
from .lease import Lease
from .authentication import SharedKeyCredentials

__all__ = [
    'BlobServiceClient',
    'ContainerClient',
    'BlobClient',
    'BlobType',
    'Lease',
]