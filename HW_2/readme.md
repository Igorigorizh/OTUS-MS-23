## k8s version of Home work 1c. Reuses image igorizhov/otus_ms_23_hw_1c from docker hub. Uses git clone subfolder copy feature with sparse.

### Run docker container with health service on port 8000
$docker run -d -p 8000:8000 igorizhov/otus_ms_23_hw_1c

curl check with $curl localhost:8000/health/

also possible to check with fastApi swagger at http://localhost:8000/docs 