import React, { useState } from 'react';
import { DateRangePicker } from 'react-date-range';
import 'react-date-range/dist/styles.css'; // main css file
import 'react-date-range/dist/theme/default.css'; // theme css file
import { useApi } from '../contexts/ApiProvider';
import { useFlash } from '../contexts/FlashProvider';

export default function Greeting(){

  const today = new Date();

  const [dateRanges, setDateRanges] = useState([
        {
      startDate: today,
      endDate: today,
      key: 'initial',
    },
  ]);
  const api = useApi();
  const flash = useFlash;

  // Handle date range selection
  const handleRangeChange = async (item) => {

    const newRange = {
      startDate: item.initial.startDate,
      endDate: item.initial.endDate,
      key: Date.now().toString()
    };


    // Send the new date range to the server
    const response = await api.post('/add-availability-range', newRange);

    if (response.ok){
      // Update the local date ranges state
      setDateRanges([...dateRanges, newRange]);
      flash('New Data successfully added', 'success');
      }
    else {
      flash('Adding Date failed', 'danger');
    }

  };

  return (
      <>
      <h1>Choose your availabilities</h1>
      <DateRangePicker
        onChange={handleRangeChange}
        showSelectionPreview={false}
        moveRangeOnFirstSelection={true}
        months={1}
        ranges={dateRanges}
        direction="horizontal"
      />
      </>
  );
}
