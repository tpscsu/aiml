import array

parking_lot = array.array('i', [1, 0, 0, 0, 0, 0, 1, 1, 0])
parking_lot.append(0)
total_spots = len(parking_lot)
occupied_spots = sum(parking_lot)
available_spot_count = total_spots - occupied_spots
print('Available Spots in the Lot {}'.format(available_spot_count))
