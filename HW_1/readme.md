### Build image
local build image:  $docker-compose build or $docker compose build

to get image from docker hub: $docker pull igorizhov/otus_ms_23_hw_1:latest

### label otus_bld_ver
arg label otus_bld_ver is used for setting the cutting cache point as a time stamp, so when active cache is disabled after the otus_bld_ver  

local build with cache cut lable: docker compose build--build-arg otus_bld_ver=$(date +%Y-%s)

### Run service 
$docker-compose up -d
or $docker compose up -d


### Run service without build pulling the image from docker hub
$docker-compose up -d --no-build 
or $docker compose up -d --no-build
