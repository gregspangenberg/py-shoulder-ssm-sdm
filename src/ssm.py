import numpy as np 

def write_vtk_shape(file_name, nodes, polys, output_path = None):

    if output_path != None:
        f = open(output_path +'/'+ file_name,'w')
        
    else:
        f = open(file_name,'w') #file will be written to root

    f.write('# vtk DataFile Version 4.2\nvtk output\nASCII\nDATASET POLYDATA\n')
    num_r,num_c, = nodes.shape
    f.write('POINTS '+ str(num_c) +' float\n')
    for idx,val in np.ndenumerate(nodes):
        node_sig= "{:.6f}".format(val)
        f.write(str(node_sig)+' ')
        if (idx[-1]+1)%9 == 0: #if index divisible by 9 then new line
            f.write('\n')
    columns_len = len(polys)
    f.write('\nPOLYGONS '+str(columns_len)+' '+str(columns_len*4))
    for idx,val in np.ndenumerate(polys):
        if (idx[-1])%3 == 0: #if 3 numbers have occured then new line
            f.write('\n')
        if (idx[-1])%3 == 0: #if index is past 3 then print 3
            f.write('3 ')
        f.write(str(val)+' ')

def humerus(perturbed_scores, file_name, output_path=None):
    """Creates a humerus given an array of size ( 1,5 )

    Args:
        perturbed_scores (numpy.ndarray): 1,5 [PC0, PC1, PC2, PC3, PC4] array of scores specify the standard deviation from the mean for 5 principal components.
        file_name (string): base name of the output files
        output_path (string, optional): output path for created .vtk files. Defaults to /vtk.

    PC0: Overall scaling; increase in size\n
    PC1: Axial elongation and medial rotation of the humeral head\n
    PC2: Generally, an increase of overall girth\n
    PC3: Increase of humeral retroversion\n
    PC4: Lateral bowing of the humeral shaft\n
    """

    output_file_name =  file_name+'-'+str(perturbed_scores)+'.vtk'
    
    coeff = np.load('./SSM/humerus/input/coeff.npy')
    scores_std = np.load('./SSM/humerus/input/scores_std.npy')
    elements = np.load('./SSM/humerus/input/elements.npy')# mean sample which is manipulated
    pc_sign_humerus_shape = np.load('./SSM/humerus/input/pc_sign_humerus_shape.npy') # enusres that positive std's are associated with increases
    humerus_shape_mean = np.load('./SSM/humerus/input/humerus_shape_mean.npy').transpose() #mean of points on all 54 samples

    scores_mapped = np.zeros_like(perturbed_scores)

    for idx,score_disturb in enumerate(perturbed_scores):
        scores_mapped[idx] = np.multiply((scores_std[idx]),pc_sign_humerus_shape[idx])*score_disturb

    nodes_no_mean = np.matmul(np.transpose(scores_mapped),np.transpose(coeff[:,0:scores_mapped.size]))
    nodes_mean = np.add(nodes_no_mean,humerus_shape_mean)
    nodes_reshape = np.reshape(nodes_mean,(3,-1))
  
    write_vtk_shape(output_file_name,nodes_reshape,elements,output_path)


def scapula(perturbed_scores, file_name, output_path=None):
    """Creates a scapula given an array of size ( 1,9 )

    Args:
        perturbed_scores (numpy.ndarray): 1,5 [PC0, PC1, PC2, PC3, PC4] array of scores specify the standard deviation from the mean for 5 principal components.
        file_name (string): base name of the output files
        output_path (string, optional): output path for created .vtk files. Defaults to /vtk.

    PC0: Overall scaling; increase in size\n
    PC1: Axial elongation and medial rotation of the humeral head\n
    PC2: Generally, an increase of overall girth\n
    PC3: Increase of humeral retroversion\n
    PC4: Lateral bowing of the humeral shaft\n
    """

    output_file_name =  file_name+'-'+str(perturbed_scores)+'.vtk'
    
    coeff = np.load('./SSM/scapula/input/coeff.npy')
    scores_std = np.load('./SSM/scapula/input/scores_std.npy')
    elements = np.load('./SSM/scapula/input/elements.npy')# mean sample which is manipulated
    pc_sign_scapula_shape = np.load('./SSM/scapula/input/pc_sign_scapula_shape.npy') # enusres that positive std's are associated with increases
    scapula_shape_mean = np.load('./SSM/scapula/input/scapula_shape_mean.npy').transpose() #mean of points on all 54 samples

    scores_mapped = np.zeros_like(perturbed_scores)

    for idx,score_disturb in enumerate(perturbed_scores):
        scores_mapped[idx] = np.multiply((scores_std[idx]),pc_sign_scapula_shape[idx])*score_disturb
    
    nodes_no_mean = np.matmul(np.transpose(scores_mapped),np.transpose(coeff[:,0:scores_mapped.size]))
    nodes_mean = np.add(nodes_no_mean,scapula_shape_mean)
    nodes_reshape = np.reshape(nodes_mean,(3,-1))

    write_vtk_shape(output_file_name,nodes_reshape,elements,output_path)