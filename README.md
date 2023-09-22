# About
Created an OTP authentication API that can be used to secure application services and enable user authentication. This API has two endpoints, which I'll describe in more detail:

Endpoint 1 - Send OTP:

- This endpoint supports a POST request, where users provide their mobile number to the backend server.
- After receiving the mobile number, the backend generates a 6-digit OTP using a Python random function.
- The OTP is then saved in a temporary database, and I have wisely used MongoDB's TTL (Time-To-Live) index feature to create this temporary database. This ensures that the OTP will expire after a set period.
- Next, the 6-digit OTP is sent to the user's mobile number using the AWS SNS service, which delivers the OTP to the user via a messaging service.

Endpoint 2 - Verify OTP:

- Users use this endpoint to submit the OTP they received via their mobile number.
- The user submits both the OTP and their mobile number.
- The backend validates whether the OTP and mobile number match the records in the temporary database and whether the OTP is still valid.
- If the OTP is submitted after its expiration time, the backend responds with "invalid credentials."
