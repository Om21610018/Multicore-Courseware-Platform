import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import React, { useState, useEffect } from 'react';

function Navigation() {
    const [isAuth, setIsAuth] = useState(false);
    useEffect(() => {
        if (localStorage.getItem('access_token') !== null) {
            setIsAuth(true);
        }
    }, [isAuth]);
    return (
        <Navbar bg="primary" variant="dark" sticky="top">
            <Container>
                <Navbar.Brand href="/">Multicore-courseware</Navbar.Brand>
                <Nav className="me-auto">
                    {isAuth ? <Nav.Link href="/">Home</Nav.Link> : null}
                    {isAuth ? (
                        <Nav.Link href="/logout">Logout</Nav.Link>
                    ) : (
                        <Nav.Link href="/login">Login</Nav.Link>
                    )}
                </Nav>
            </Container>
        </Navbar>
    );
};

export default Navigation;