import sdm
import ssm
import time

t0 = time.time()
#define a bunch of principal comonent arrays6
# pcs = np.round(np.random.uniform(low=0, high=2, size=(100,5)),3)
pcs = [[1,1,1,1,1.2,1.2,1.1,0.9,0.8,0.7]]
for pc in pcs:
    sdm.humerus(pc,'humerus',output_path=r'.\SDM\humerus\vtk')

t1 = time.time()
print(t1-t0)