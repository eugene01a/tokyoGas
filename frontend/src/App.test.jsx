import React from 'react';
import '@testing-library/jest-dom';
import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

// Basic tests for React form validation and rendering.
describe('React registration form', () => {
  it('renders the registration form', () => {
    render(<App />);
    expect(screen.getByLabelText(/username/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
  });

  it('shows validation messages for invalid input', () => {
    render(<App />);
    fireEvent.change(screen.getByLabelText(/username/i), { target: { value: 'ab' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'wrong' } });
    fireEvent.change(screen.getByLabelText(/password/i), { target: { value: 'weak' } });
    fireEvent.change(screen.getByLabelText(/tel/i), { target: { value: '090-123' } });
    fireEvent.change(screen.getByLabelText(/prefecture/i), { target: { value: '' } });
    fireEvent.click(screen.getByRole('button', { name: /register/i }));

    expect(screen.getByText(/username must be at least 3 characters long/i)).toBeInTheDocument();
    expect(screen.getByText(/enter a valid email address/i)).toBeInTheDocument();
    expect(screen.getByText(/password must be at least 8 characters long/i)).toBeInTheDocument();
    expect(screen.getByText(/telephone number must contain digits only/i)).toBeInTheDocument();
    expect(screen.getByText(/please select a prefecture/i)).toBeInTheDocument();
  });
});
