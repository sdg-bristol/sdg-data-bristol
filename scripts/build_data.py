from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    print(meta)
    for i in range(1,5):
        if "source_organisation_"+str(i) in meta:
            meta["source_active_"+str(i)] = True
    if meta["data_non_statistical"] == "Y":
        meta["data_non_statistical"] == True
    else:
        meta["data_non_statistical"] == False
    if meta["data_show_map"] == "Y":
        meta["data_non_statistical"] == True
    else:
        meta["data_show_map"] == False
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
