import React, { useState, useEffect } from 'react';
import { DateRangePicker } from 'react-date-range';
import 'react-date-range/dist/styles.css'; // main css file
import 'react-date-range/dist/theme/default.css'; // theme css file
import { useApi } from '../contexts/ApiProvider';
import { useFlash } from '../contexts/FlashProvider';

export default function KeyCalendar(){

  const today = new Date();

  const default_range = {
      startDate: today,
      endDate: today,
      key: 'initial',
    }

  const [dateRanges, setDateRanges] = useState([
        default_range,
  ]);
  const api = useApi();
  const flash = useFlash;

  useEffect(() => {
    (async () => {
      const response = await api.get('/availability-ranges');
      if (response.ok) {
        const ranges = response.body
        const helper_range = {
            startDate: today,
            endDate: today,
            key: 'initial',
          }

        const updatedData = ranges.map(item => {
          const startDate = new Date(item.startDate);
          const endDate = new Date(item.endDate);

          return {
            ...item,
            startDate,
            endDate
          };
        });

        const full_ranges = [...updatedData, helper_range];
        setDateRanges(full_ranges);
      }
      else {
        flash('Couldnt load', 'danger');
      }
    })();
  }, [api, flash]);

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
      <div className="custom-date-range-picker">
      <h1>Choose your availabilities</h1>
      <DateRangePicker
        onChange={handleRangeChange}
        showSelectionPreview={false}
        moveRangeOnFirstSelection={true}
        showMonthAndYearPickers={true}
        showDateDisplay={false}
        timeZone="UTC"
        months={1}
        ranges={dateRanges}
        direction="horizontal"
      />
      </div>
  );
}
