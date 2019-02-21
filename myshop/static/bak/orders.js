window.onload = function() {
  "use strict";

  const sumCalculator = {
    settings: {
      rowsDataName: 'formset_row',
      totalCostEl: document.querySelector('.order_total_cost'),
      totalQuantityEl: document.querySelector('.order_total_quantity'),
      tableEl: document.querySelector('table')
    },
    sumPrice: null,
    sumQuantity: null,

    init() {
      this.rowsWithDataInputs = this.settings.tableEl.querySelectorAll(`.${this.settings.rowsDataName}`);
      this.addListeners();
    },

    addListeners() {
      let quantityElems = document.querySelectorAll('[data-quantity]');
      for (let el of quantityElems) {
        el.addEventListener('input', (event) => this.quantityListener(event));
      }
    },

    quantityListener(event) {
      let quantity = event.target.value;
      event.target.parentElement.setAttribute('data-quantity', quantity);
      this.calculateSum();
      this.renderSum();
    },

    calculateSum() {
      this.setNullSum();
      for (let row of this.rowsWithDataInputs) {
        try {
          let price = row.querySelector('[data-price]').dataset.price;
          let quantity = row.querySelector('[data-quantity]').dataset.quantity;
          if (price) {
             let temp = price * quantity;
             this.sumPrice += temp;
             this.sumQuantity += +quantity;
          }
        } catch(TypeError) {
          break
        }
      }
    },

    renderSum() {
      this.settings.totalCostEl.textContent = this.sumPrice;
      this.settings.totalQuantityEl.textContent = this.sumQuantity;
    },

    setNullSum() {
      this.sumPrice = 0;
      this.sumQuantity = 0
    }
  };

  sumCalculator.init();
}

