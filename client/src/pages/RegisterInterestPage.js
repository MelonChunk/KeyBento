import { useEffect, useRef } from 'react';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Body from '../components/Body';

import InputField from '../components/InputField';
import { useFlash } from '../contexts/FlashProvider';
import { useApi } from '../contexts/ApiProvider';


export default function RegisterInterestPage() {
  const api = useApi();
  const flash = useFlash();

  const nameField = useRef();
  const emailField = useRef();
  const commentField = useRef();

  useEffect(() => {
    nameField.current.focus();
  }, []);

  const onSubmit = async (ev) => {
    ev.preventDefault();
    const response = await api.post("/notification_of_interest", {
      name: nameField.current.value,
      email:emailField.current.value,
      comment:commentField.current.value,
    });
    if (response.ok) {
      flash('Thank you for registering your interest', 'success');
    }
    else {
      flash('It seems your email is already registered', 'danger');
    }

  };

  return (
    <Body>
    <h1>Keep me updated!</h1>
    <Form onSubmit={onSubmit}>
      <InputField
        name="name" label="Name" fieldRef={nameField} />
      <InputField
        name="email" label="Email" fieldRef={emailField} />
      <InputField
        name="comment" label="Comments"  fieldRef={commentField} />
      <Button variant="primary" type="submit">Register interest</Button>
    </Form>
    </Body>
  );
}
