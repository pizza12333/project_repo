sudo apt-get gcc -y
sudo apt-get g++ -y
sudo apt-get make -y

mkdir downloads
cd downloads

wget https://repo.continuum.io/archive/Anaconda2-4.4.0-Linux-x86_64.sh
yes | "yes" Anaconda2-4.4.0-Linux-x86_64.sh

source ~/.bashrc

echo "compelet ananconda install"
conda 

