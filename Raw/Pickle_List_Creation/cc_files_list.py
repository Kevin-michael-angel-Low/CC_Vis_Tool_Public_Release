import glob
import pickle

print("running...")
# glob_files = glob.glob(r"/Volumes/faculty/njahansh/nerds/alyssa/corpus_callosum/UKBB/bfcorr_results/*/segmentation/*/*_std_BF_adj_flirt.nii.gz", recursive = True)
# print(glob_files)

i = 0

cc_files = []

for filename in glob.iglob(r"/Volumes/faculty/njahansh/nerds/alyssa/corpus_callosum/UKBB/bfcorr_results/*/segmentation/*/*_std_BF_adj_flirt_cc.nii.gz", recursive = True):
    cc_files.append(filename)
    cc_files.sort()
    i = i + 1
    print("adding" + filename)
    print("On file # " + str(i))

with open ('cc_30k.pkl', 'wb') as filehandle:
    pickle.dump(cc_files, filehandle)
print("Pickle list creation complete!")