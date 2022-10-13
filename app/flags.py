import os
import json
from pathlib import Path

from tklauthtools.feature_flags import FeatureFlagService

from app.secrets import get_secret

def init_feature_flags():
    found_key = get_secret(os.environ.get("LD_SDK_KEY_PATH", "dev/launch-darkly/sdk-key"))
    key = json.loads(found_key)["LD_SDK_KEY"]
    local_flag_file = os.environ.get("LAUNCHDARKLY_LOCAL_FLAG_FILE")
    if local_flag_file is not None and not Path(local_flag_file).exists():
        local_flag_file = None

    return FeatureFlagService(key, local_flag_file)
