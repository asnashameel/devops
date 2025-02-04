# Description: Navigates to the Desktop folder of the current user.


try {
    $identity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object System.Security.Principal.WindowsPrincipal($identity)
    $isAdmin = $principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)

if ($isAdmin) {
    Write-Output "The current user has admin access."
} else {
    Write-Output "The current user does NOT have admin access."
}
} catch {
    "error i line $($_.InvocationInfo.ScriptLineNumber) : $($Error[0])"
}