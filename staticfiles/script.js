const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});




document.addEventListener("DOMContentLoaded", function () {
  const carImages = {
    "SUV": { src: "images/suv.jpg", alt: "SUV" },
    "VAN": { src: "images/van.jpg", alt: "VAN" },
    "PICK-UP TRUCK": { src: "images/pickup_truck.jpg", alt: "PICK-TRUCK" },
    "Flatbed Trucks": { src: "images/Flatbed.jpg", alt: "Flatbed Trucks" },
  };

  //  BOOKING PAGE FUNCTIONALITY
  if (document.getElementById("booking-form")) {
    const bookingForm = document.getElementById("booking-form");

    function generateRequestId() {
      const randomNum = Math.floor(10000000 + Math.random() * 90000000);
      return "#" + randomNum.toString();
    }

    function formatDate(dateStr) {
      const d = new Date(dateStr);
      if (isNaN(d)) return "";
      const day = String(d.getDate()).padStart(2, "0");
      const month = String(d.getMonth() + 1).padStart(2, "0");
      const year = String(d.getFullYear()).slice(-2);
      return `${day}/${month}/${year}`;
    }

    function addBooking(e) {
      e.preventDefault();

      const userName = document.getElementById("user-name").value.trim();
      const destination = document.getElementById("destination").value.trim();
      const pickupDate = document.getElementById("pickup-date").value;
      const returnDate = document.getElementById("return-date").value;
      const typeCar = document.getElementById("type-car").value;

      if (!userName || !destination || !pickupDate || !returnDate || !typeCar) {
        alert("Please fill in all fields.");
        return false;
      }

      const formattedPickupDate = formatDate(pickupDate);
      const formattedReturnDate = formatDate(returnDate);
      const requestId = generateRequestId();

      const booking = {
        id: requestId,
        user: userName,
        destination,
        pickupDate: formattedPickupDate,
        returnDate: formattedReturnDate,
        vehicle: typeCar,
        image: carImages[typeCar] ? carImages[typeCar].src : "https://placehold.co/60x30?text=No+Image",
        timeBooked: new Date().toLocaleString(),
        approved: false
      };

      const bookings = JSON.parse(localStorage.getItem("bookings")) || [];
      bookings.push(booking);
      localStorage.setItem("bookings", JSON.stringify(bookings));

      const pendingBookings = JSON.parse(localStorage.getItem("pendingBookings")) || [];
      pendingBookings.push(booking);
      localStorage.setItem("pendingBookings", JSON.stringify(pendingBookings));

      alert("Book Reservation submit.");
    }

    bookingForm.addEventListener("submit", addBooking);
  }

  //  APPROVAL PAGE FUNCTIONALITY
  if (document.getElementById("approval-tbody")) {
    const approvalTableBody = document.getElementById("approval-tbody");
    const searchInput = document.getElementById("search-input");

    let pendingBookings = JSON.parse(localStorage.getItem("pendingBookings")) || [];

    function renderTable(data) {
      approvalTableBody.innerHTML = "";
      if (data.length === 0) {
        approvalTableBody.innerHTML = "<tr><td colspan='10'>No pending bookings.</td></tr>";
        return;
      }

      data.forEach((booking) => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${booking.id}</td>
          <td>${booking.user}</td>
          <td>${booking.vehicle}</td>
          <td>${booking.destination}</td>
          <td>${booking.pickupDate}</td>
          <td>${booking.returnDate}</td>
          <td><img src="${booking.image}" alt="${booking.vehicle}" height="30" width="60"></td>
          <td>${booking.timeBooked}</td>
          <td>
            <button class="approve-btn">Approve</button>
            <button class="reject-btn">Reject</button>
            <span class="status-text"></span>
          </td>
        `;
        approvalTableBody.appendChild(tr);

        const approveBtn = tr.querySelector(".approve-btn");
        const rejectBtn = tr.querySelector(".reject-btn");
        const statusText = tr.querySelector(".status-text");

        approveBtn.addEventListener("click", () => {
          statusText.textContent = "Approved";
          statusText.style.color = "green";
          saveToHistory("approvedBookings", booking);
          removeBookingById(booking.id);
        });

        rejectBtn.addEventListener("click", () => {
          statusText.textContent = "Rejected";
          statusText.style.color = "red";
          saveToHistory("rejectedBookings", booking);
          removeBookingById(booking.id);
        });
      });
    }

    function saveToHistory(key, booking) {
      const current = JSON.parse(localStorage.getItem(key)) || [];
      booking.status = key === "approvedBookings" ? "Approved" : "Rejected";
      current.push(booking);
      localStorage.setItem(key, JSON.stringify(current));
    }

    function removeBookingById(id) {
      pendingBookings = pendingBookings.filter((b) => b.id !== id);
      localStorage.setItem("pendingBookings", JSON.stringify(pendingBookings));
      renderTable(pendingBookings);
    }

    searchInput.addEventListener("input", () => {
      const keyword = searchInput.value.toLowerCase();
      const filtered = pendingBookings.filter(b =>
        b.user.toLowerCase().includes(keyword) ||
        b.vehicle.toLowerCase().includes(keyword) ||
        b.destination.toLowerCase().includes(keyword)
      );
      renderTable(filtered);
    });

    renderTable(pendingBookings);
  }

  //  HISTORY PAGE FUNCTIONALITY
  if (document.getElementById("approved-tbody") && document.getElementById("rejected-tbody")) {
    const approvedTbody = document.getElementById("approved-tbody");
    const rejectedTbody = document.getElementById("rejected-tbody");

    const approved = JSON.parse(localStorage.getItem("approvedBookings")) || [];
    const rejected = JSON.parse(localStorage.getItem("rejectedBookings")) || [];

    function renderTable(data, tbody) {
      tbody.innerHTML = "";
      if (data.length === 0) {
        tbody.innerHTML = "<tr><td colspan='7'>No data found.</td></tr>";
        return;
      }

      data.forEach((booking) => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${booking.id}</td>
          <td>${booking.user}</td>
          <td>${booking.vehicle}</td>
          <td>${booking.destination}</td>
          <td>${booking.pickupDate}</td>
          <td>${booking.returnDate}</td>
          <td><img src="${booking.image}" alt="${booking.vehicle}" height="30" width="60"></td>
        `;
        tbody.appendChild(tr);
      });
    }

    renderTable(approved, approvedTbody);
    renderTable(rejected, rejectedTbody);
  }
});


function resetBookingHistory() {
  const approvedTbody = document.getElementById('approved-tbody');
  const rejectedTbody = document.getElementById('rejected-tbody');

  localStorage.removeItem('approvedBookings');
  localStorage.removeItem('rejectedBookings');


  approvedTbody.innerHTML = `
    <tr>
      <td colspan="7" style="text-align: center;">No data found.</td>
    </tr>
  `;

  rejectedTbody.innerHTML = `
    <tr>
      <td colspan="7" style="text-align: center;">No data found.</td>
    </tr>
  `;

  alert('Booking history has been reset.');
}


//Utility functions 
function goBackToBooking() {
  window.location.href = "booking.html";
}

function resetPending() {
  localStorage.removeItem("pendingBookings");
  location.reload();
}

function goBack() {
  window.history.back();
}
