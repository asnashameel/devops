# Description: Navigates to the Desktop folder of the current user.


try {
    $Path=[Environment]::GetFolderPath("asna")
    echo $Path
if (Test-Path "$env:USERPROFILE\Desktop") {
    Set-Location "$env:USERPROFILE\Desktop"
    Write-Host "Navigated to Desktop."
    } else  {
    Write-Host "Desktop folder does not exist."
    }
} catch {
    "error i line $($_.InvocationInfo.ScriptLineNumber) : $($Error[0])"
}

