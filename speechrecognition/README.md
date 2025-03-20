## Creat VENV
use the `create_env.sh` script to create a venv on windows 11

```powershell
cd $env:USERPROFILE\Documents\VCS\llm-train;

$VERSION="3.12";
$ENV_NAME="azureai";
$ENV_SURFIX="pip";
$PM="pip";
$WORK_DIR="$env:USERPROFILE\Documents\VENV\";
.\envtools\create_env.ps1 -VERSION $VERSION -ENV_NAME $ENV_NAME -ENV_SURFIX $ENV_SURFIX -PM $PM -WORK_DIR $WORK_DIR;
```

## Install the package
```powershell
cd $env:USERPROFILE\Documents\VCS\ai-demos\speechrecognition;

$VERSION="3.12";
$ENV_NAME="azureai";
$ENV_SURFIX="pip";
$ENV_FULL_NAME = "$ENV_NAME$VERSION$ENV_SURFIX";
$PackageFile="requirements.txt";
& "$env:USERPROFILE\Documents\VENV\$ENV_FULL_NAME\Scripts\Activate.ps1";
Invoke-Expression "(Get-Command python).Source";

& "python" -m pip install --upgrade pip;
& "python" -m pip install -r $PackageFile --no-cache-dir;

deactivate
```

## Reference
* https://raw.githubusercontent.com/Azure-Samples/cognitive-services-speech-sdk/refs/heads/master/samples/python/console/speech_language_detection_sample.py