<?php

use Symfony\Component\HttpFoundation\Cookie;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

public function checkCookie(Request $request): Response
{
    $response = $this->render('/welcome.html');

    if (!$request->cookies->has('PHPSESSID')) {
        $sessionId = bin2hex(random_bytes(32)); // Generate a secure random session ID
        $cookie = Cookie::create('PHPSESSID', $sessionId, 0, '/', null, false, true); // Set secure and httpOnly flags
        $response->headers->setCookie($cookie);
    }

    return $response;
}

?>