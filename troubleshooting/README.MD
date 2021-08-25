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

### Unable to locate package nvidia-container-runtime
this warned, when u send:
```
sudo apt-get install nvidia-container-runtime
```
Run this:
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
sudo apt-get install nvidia-container-runtime
```
https://github.com/NVIDIA/nvidia-docker/issues/1238

### No CUDA GPU detected!
, diagnostics: cudaError_t 804 : "forward compatibility was attempted on non supported HW", in cu-device.cc:185
```
ubuntu-drivers devices
sudo apt install nvidia-driver-470
sudo reboot now
```

