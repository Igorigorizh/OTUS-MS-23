## k8s version of Home work 1c. Reuses image igorizhov/otus_ms_23_hw_1c from docker hub. Uses git clone subfolder copy feature with sparse.

### Start application with health check on port 8000 with readiness and liveness probe 
$kubectl apply -f .

curl check: $curl arch.homework:8000/health/ -> OK

rewrite: arch.homework:8000/otusapp/igor/health - still not works???
 