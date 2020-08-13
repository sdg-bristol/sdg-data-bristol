from sdg.open_sdg import open_sdg_check


def alter_meta(meta):
    for i in range(1,5):
        if "source_active_"+str(i) in meta:
            if meta["source_active_"+str(i)] == "true":
                meta["source_active_"+str(i)] = 'custom.True'
    return meta

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_meta=alter_meta)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
