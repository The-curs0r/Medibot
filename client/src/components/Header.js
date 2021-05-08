import React from 'react';
import {Link} from 'react-router-dom'
import "./Header.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar,Nav,NavDropdown} from 'react-bootstrap'
const Header = ()=>{
    return(
        <Navbar bg="light" expand="lg">
			<Navbar.Brand href="/">Medibot</Navbar.Brand>
			<Navbar.Toggle aria-controls="basic-navbar-nav" />
			<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="mr-auto">
				<Nav.Link href="/">Home</Nav.Link>
				<Nav.Link href="/medibot">Bot</Nav.Link>
				</Nav>
			</Navbar.Collapse>
		</Navbar>
    )
}


export default Header;