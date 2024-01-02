
def compare_voxels(file1: str, file2: str) -> int:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        out1, x1, y1, z1 = f1.readline().split()
        out2, x2, y2, z2 = f2.readline().split()
        NumVoxel = 1
        for line1, line2 in zip(f1, f2):
            step1, mat1, den1 = line1.split()
            step2, mat2, den2 = line2.split()

            if (step1 != step2 and mat1 != mat2 and float(den1) != float(den2)):
                return False
            NumVoxel += 1
        print(f"{x1}*{y1}*{z1}={NumVoxel-1} voxels are compared")
        return True

with open('input.txt', 'r') as input:
    for line in input:
        item, ref, new = line.strip().split()
        if compare_voxels(ref, new):
            print(f"{item}: The files are identical")
        else:
            print(f"{item}: The files are different")

#input.txt
# logic_gaa_final 75.voxel voxel_job_1232800001_step_75.txt
# logic_fin_final 64.voxel voxel_job_1232800000_step_64.txt
# dram_igzo 102.voxel voxel_job_1232900000_step_102.txt
# vnand 90.voxel voxel_job_140200007_step_90.txt
