$functionName = "novaEngine"
$region = "us-central1"
$sourcePath = "C:\Path\To\Nova\nova_engine"
$entryPoint = "app"

gcloud functions deploy $functionName `
  --runtime python311 `
  --trigger-http `
  --entry-point $entryPoint `
  --region $region `
  --allow-unauthenticated `
  --source $sourcePath `
  --env-vars-file ".\deploy\.env"
