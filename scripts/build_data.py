from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    for i in range(1,5):
        if "source_active_"+str(i) in meta:
            if meta["source_active_"+str(i)] == "true":
                meta["source_active_"+str(i)] = 'custom.True'
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
