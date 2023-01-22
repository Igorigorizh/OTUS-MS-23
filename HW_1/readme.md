local build image:  docker compose build  --build-arg otus_bld_ver=$(date +%Y-%s)
get image from docker hub: docker pull igorizhov/otus_ms_23_hw_1:latest

arg label otus_bld_ver is used for setting cache point as a time stamp  
