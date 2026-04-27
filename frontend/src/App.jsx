import React, { useEffect, useState } from 'react';

const initialState = {
  username: '',
  email: '',
  password: '',
  tel: '',
  pref: '',
};

// Client-side validation matching backend rules for immediate feedback.
const validate = (values) => {
  const errors = {};
  if (!values.username || values.username.trim().length < 3) {
    errors.username = 'Username must be at least 3 characters long.';
  }
  if (!values.email || !/^\S+@\S+\.\S+$/.test(values.email)) {
    errors.email = 'Enter a valid email address.';
  }
  if (!values.password || values.password.length < 8) {
    errors.password = 'Password must be at least 8 characters long.';
  } else {
    if (!/[A-Z]/.test(values.password)) {
      errors.password = 'Password must contain at least one uppercase letter.';
    }
    if (!/[a-z]/.test(values.password)) {
      errors.password = 'Password must contain at least one lowercase letter.';
    }
    if (!/[0-9]/.test(values.password)) {
      errors.password = 'Password must contain at least one digit.';
    }
  }
  if (values.tel && !/^\d+$/.test(values.tel)) {
    errors.tel = 'Telephone number must contain digits only.';
  }
  if (!values.pref) {
    errors.pref = 'Please select a prefecture.';
  }
  return errors;
};

const DEFAULT_PREF_OPTIONS = [{ value: '', label: 'Select a prefecture' }];

export default function App() {
  const [values, setValues] = useState(initialState);
  const [errors, setErrors] = useState({});
  const [serverMessage, setServerMessage] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [prefOptions, setPrefOptions] = useState(DEFAULT_PREF_OPTIONS);

  useEffect(() => {
    fetch('/api/prefs/')
      .then((response) => response.json())
      .then((data) => {
        setPrefOptions([
          { value: '', label: 'Select a prefecture' },
          ...data.map((pref) => ({ value: String(pref.id), label: pref.name })),
        ]);
      })
      .catch(() => {
        setPrefOptions([
          { value: '', label: 'Select a prefecture' },
          { value: '1', label: 'Tokyo' },
          { value: '2', label: 'Osaka' },
          { value: '3', label: 'Kanagawa' },
        ]);
      });
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    const nextValues = { ...values, [name]: value };
    setValues(nextValues);
    setErrors(validate(nextValues));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const validationErrors = validate(values);
    setErrors(validationErrors);
    if (Object.keys(validationErrors).length > 0) {
      return;
    }

    const response = await fetch('/api/register/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: values.username,
        email: values.email,
        password: values.password,
        tel: values.tel,
        pref: values.pref,
      }),
    });

    if (response.ok) {
      setServerMessage('Registration complete.');
      setSubmitted(true);
      setValues(initialState);
    } else {
      const data = await response.json();
      setServerMessage('Registration failed.');
      setErrors(data);
    }
  };

  if (submitted) {
    return (
      <main className="container">
        <h1>Registration Complete</h1>
        <p>Your account has been successfully created.</p>
        <button onClick={() => setSubmitted(false)}>Register another user</button>
      </main>
    );
  }

  return (
    <main className="container">
      <h1>React User Registration</h1>
      <form onSubmit={handleSubmit} noValidate>
        <div className="field">
          <label htmlFor="username">Username</label>
          <input name="username" id="username" value={values.username} onChange={handleChange} />
          {errors.username && <div className="error">{errors.username}</div>}
        </div>
        <div className="field">
          <label htmlFor="email">Email</label>
          <input name="email" id="email" value={values.email} onChange={handleChange} />
          {errors.email && <div className="error">{errors.email}</div>}
        </div>
        <div className="field">
          <label htmlFor="password">Password</label>
          <input type="password" name="password" id="password" value={values.password} onChange={handleChange} />
          {errors.password && <div className="error">{errors.password}</div>}
        </div>
        <div className="field">
          <label htmlFor="tel">Telephone</label>
          <input name="tel" id="tel" value={values.tel} onChange={handleChange} />
          {errors.tel && <div className="error">{errors.tel}</div>}
        </div>
        <div className="field">
          <label htmlFor="pref">Prefecture</label>
          <select name="pref" id="pref" value={values.pref} onChange={handleChange}>
            {prefOptions.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
          {errors.pref && <div className="error">{errors.pref}</div>}
        </div>
        <button type="submit">Register</button>
      </form>
      {serverMessage && <p className="server-message">{serverMessage}</p>}
    </main>
  );
}
