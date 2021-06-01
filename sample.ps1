Copy-Item -Path /var/lib/jenkins/workspace/sample1/  -Destination /root/backup/$(Get-Date -format "dd-MM-yyyy") -Recurse
