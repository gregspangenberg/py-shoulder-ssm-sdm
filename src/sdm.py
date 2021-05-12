import numpy as np
import shutil

def write_vtk_density(densities, input_file_path,output_dir_path,output_file_name):
    """Creates the .vtk file form the calculated matrix data

    Args:
        densities (array): density data
        input_file_path (str_path): path to input file
        output_dir_path (str_path, optional): Output path for files. Defaults to None.
        output_file_name (str,optional): Name of the file. Defulats to None and appends to the existing file. 
    """
    output_file_path = output_dir_path+'/'+output_file_name
    shutil.copy(input_file_path, output_file_path)
    f = open(output_file_path,'a')
    
    f.write('POINT_DATA ' + str(densities.size)+'\n') #densities must be a numpy array of size(1,n)
    f.write('SCALARS Density' + ' float\n')
    f.write('LOOKUP_TABLE default\n')
    for idx,val in np.ndenumerate(densities):
        val_sig= "{:.6f}".format(val)   #6 decimal points
        f.write(str(val_sig)+' ')
        if (idx[-1]+1) % 9 == 0:
            f.write('\n') 


def humerus(perturbed_scores, file_name, output_path=None):
    """Creates a humerus with varied density given an array of size ( 1,10 )

    Args:
        perturbed_scores (numpy.ndarray): array of scores that specify the stadrad deviations away from the mean each principal component will be
        file_name (string): base name of the output files
        output_path (string, optional): output path for created .vtk files. Defaults to None.
    """
    output_file_name =  file_name+'-'+str(perturbed_scores)+'.vtk'

    coeff = np.load('./SDM/humerus/input/coeff.npy')
    scores_std = np.load('./SDM/humerus/input/scores_std.npy') 
    pc_sign_humerus_density = np.load('./SDM/humerus/input/pc_sign_humerus_density.npy')
    humerus_density_mean = np.load('./SDM/humerus/input/humerus_density_mean.npy').transpose()

    scores_mapped = np.zeros_like(perturbed_scores)
    
    for idx,score_disturb in enumerate(perturbed_scores):
        scores_mapped[idx] = np.multiply(scores_std[idx]),pc_sign_humerus_density[idx])*score_disturb
        
    
    density_no_mean = np.matmul(np.transpose(scores_mapped),np.transpose(coeff[:,0:scores_mapped.size]))
    density_mean = np.add(density_no_mean,humerus_density_mean)
    write_vtk_density(density_mean,'./SDM/humerus/input/Average_Mesh_Humerus.vtk',output_path,output_file_name)

def scapula(perturbed_scores, file_name, output_path=None):
    """Creates a scapula with varied density given an array of size ( 1,17 )

    Args:
        perturbed_scores (numpy.ndarray): array of scores that specify the stadrad deviations away from the mean each principal component will be
        file_name (string): base name of the output files
        output_path (string, optional): output path for created .vtk files. Defaults to None.
    """
    output_file_name =  file_name+'-'+str(perturbed_scores)+'.vtk'

    coeff = np.load('./SDM/scapula/input/coeff.npy')
    scores_std = np.load('./SDM/scapula/input/scores_std.npy') 
    pc_sign_scapula_density = np.load('./SDM/scapula/input/pc_sign_scapula_density.npy')
    scapula_density_mean = np.load('./SDM/scapula/input/scapula_density_mean.npy').transpose()

    scores_mapped = np.zeros_like(perturbed_scores)
    
    for idx,score_disturb in enumerate(perturbed_scores):
        scores_mapped[idx] = np.multiply(scores_std[idx]),pc_sign_scapula_density[idx])*score_disturb
        
    
    density_no_mean = np.matmul(np.transpose(scores_mapped),np.transpose(coeff[:,0:scores_mapped.size]))
    density_mean = np.add(density_no_mean,scapula_density_mean)
    write_vtk_density(density_mean,'./SDM//scapula/input/Average_Mesh_scapula.vtk',output_path,output_file_name)