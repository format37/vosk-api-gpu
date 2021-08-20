To check docker-compose gpu support, run:
```
docker-compose up
```
If u get an error
```
ERROR: for troubleshooting_test_1  Cannot create container for service test: Unknown runtime specified nvidia

ERROR: for test  Cannot create container for service test: Unknown runtime specified nvidia
ERROR: Encountered errors while bringing up the project.
```
then follow: https://docs.docker.com/compose/gpu-support/   
And: https://github.com/nvidia/nvidia-container-runtime#docker-engine-setup   
   
### unmet dependencies
The following packages have unmet dependencies   
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).   
```
sudo apt purge -f libnvidia-encode-440 libnvidia-decode-440 cuda-drivers nvidia-driver-440 cuda-runtime-10-1 cuda-10-1 cuda-demo-suite-10-1
```
https://askubuntu.com/questions/1288124/how-to-remove-conflicting-nvidia-packages-and-unmet-dependencies/1298940#1298940
