# Set your GCP project
$project = "silent-revolution-ai-nexus"

# Create secrets and upload local values
$secrets = @{
    "openai_yourbirthplace" = "sk-xxx-your-openai-key"
    "claud_secret" = "your-claude-token"
    "nova_gemini_acces" = "your-gemini-access-token"
    "Nova-Plugin-Pem" = "-----BEGIN CERTIFICATE-----`n...`n-----END CERTIFICATE-----"
}

foreach ($name in $secrets.Keys) {
    Write-Host "Creating secret: $name"
    $value = $secrets[$name]
    $tmp = "$env:TEMP\$name.txt"
    $value | Out-File -Encoding ascii -FilePath $tmp
    gcloud secrets create $name --project=$project --replication-policy="automatic" --data-file=$tmp
    Remove-Item $tmp
}
