import { useState, useEffect, useRef } from 'react';
import Stack from "react-bootstrap/Stack";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputField from './InputField';
import { useApi } from '../contexts/ApiProvider';
import { useFlash } from '../contexts/FlashProvider';

export default function AddProperty({ showProperty }) {
  const [formErrors, setFormErrors] = useState({});
  const flash = useFlash();
  const typeField = useRef();
  const cityField = useRef();
  const countryField = useRef();
  const addressField = useRef();
  const descriptionField = useRef();

  let fields = [typeField, cityField, countryField, addressField, descriptionField]

  const api = useApi();

  function nullField(field){
    field.current.value = ''
  }

  useEffect(() => {
    typeField.current.focus();
  }, []);

  const onSubmit = async (ev) => {
    ev.preventDefault();
    const response = await api.post("/new_property", {
      type: typeField.current.value,
      city: cityField.current.value,
      country: countryField.current.value,
      address: addressField.current.value,
      description: descriptionField.current.value
    });
    if (response.ok) {
      showProperty(response.body);
      fields.forEach(nullField);
      flash('Your new property has been added', 'success')
    }
    else {
      if (response.body.errors) {
        setFormErrors(response.body.errors.json);
        flash('Adding new property failed', 'error')
      }
    }
  };

  return (
    <Stack  gap={3} className="Write">

      <Form onSubmit={onSubmit}>
        <InputField
          name="type" placeholder="What type of property? Flat or House?"
          error={formErrors.type} fieldRef={typeField} />
        <InputField
          name="city" placeholder="Which city is the property located"
          error={formErrors.city} fieldRef={cityField} />
        <InputField
          name="country" placeholder="Which country is the property located"
          error={formErrors.country} fieldRef={countryField} />
        <InputField
          name="address" placeholder="What's the address"
          error={formErrors.address} fieldRef={addressField} />
        <InputField
          name="description" placeholder="A short description of your place"
          error={formErrors.description} fieldRef={descriptionField} />
        <Button variant="primary" type="submit">Add Property</Button>
      </Form>
    </Stack>
  );
}
