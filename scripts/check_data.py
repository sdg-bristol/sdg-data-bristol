from sdg.open_sdg import open_sdg_check


def alter_meta(meta):
    print(meta)
    for i in range(1,5):
        if "source_organisation_"+str(i) in meta:
            meta["source_active_"+str(i)] = True
    if "data_non_statistical" in meta:
        if meta["data_non_statistical"] == "Y":
            meta["data_non_statistical"] = True
        elif meta["data_non_statistical"] == "N":
            meta["data_non_statistical"] = False
    else:
        meta["data_non_statistical"] = False
    return meta

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_meta=alter_meta)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
