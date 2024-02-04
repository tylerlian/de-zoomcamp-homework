if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # print('Rows with zero passengers or zero trip distance: ', {data['passenger_count'].isin([0]).sum() + data['trip_distance'].isin([0]).sum()})

    # return data.query('passenger_count > 0 and trip_distance > 0')
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    
    print(data['VendorID'].unique())
    data = data.rename(columns={
        'VendorID': 'vendor_id', 
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    })
    return data.query('passenger_count > 0 and trip_distance > 0')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert ((output['passenger_count'].isin([0]).sum() == 0) and 
        (output['trip_distance'].isin([0]).sum() == 0) and
        (output['vendor_id'].isin([1,2,None]).sum() == len(output))), 'The output is undefined'
