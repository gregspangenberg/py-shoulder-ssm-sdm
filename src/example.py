import sdm
import ssm

#define one principal comonent array
pcs = [[1,1,1,1,1.2,1.2,1.1,0.9,0.8,0.7]]
for pc in pcs:
    sdm.humerus(pc,'humerus',output_path=r'.\SDM\humerus')
    #sdm.scapula(pc,'scapula',output_path=r'.\SDM\scapula')
    #ssm.humerus(pc,'humerus',output_path=r'.\SSM\humerus')
    #ssm.scapula(pc,'scapula',output_path=r'.\SSM\scapula')

