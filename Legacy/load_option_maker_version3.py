import os

a = str(chr(92)) #円マーク(\)の文字コード

Current_directory = os.getcwd()

Sub_folder = os.walk(Current_directory)

a = str(chr(92)) #円マーク(\)の変換
dir_list = ""

for folders in Sub_folder:
    folder_dir = folders[0]
    folder_dir = folder_dir.replace(a, a+a)
    folder_dir = '"' + folder_dir + '"'
    dir_list = dir_list + " " + folder_dir

export_text = (
'LoadOptions_SearchPaths:' + dir_list +
"""
LoadOptions_LoadComponents: load_all_components
LoadOptions_LoadFully: YES
LoadOptions_UseLightweightRepresentations: YES
LoadOptions_LoadWAVE: NO
LoadOptions_LoadWAVEParents: NONE
LoadOptions_LoadSubstitution: dont_allow_substitution
LoadOptions_LoadLatest: NO
LoadOptions_LoadOption: load_from_search_dirs
LoadOptions_ManagedModeLoadOption: load_by_revision_rule
LoadOptions_LoadFilters: load_no_components
LoadOptions_LoadFailOption: dont_abort
LoadOptions_ReferenceSets: "As Saved" "Use Model" "Entire Part" "Empty" 
LoadOptions_ApplyAllLevels: NO
LoadOptions_GenerateMissingPFM: YES
LoadOptions_BookmarkRefSets: Import
LoadOptions_BookmarkPartsLoad: Load_Visible
LoadOptions_BookmarkRestoreFullyLoadedState: no
LoadOptions_SubsetLoadBehavior: Do_Not_Update
"""
)

file = open(Current_directory + '\load_options.def', 'w')
file.write(export_text)
file.close()