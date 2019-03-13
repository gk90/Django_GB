
"use strict";

const sumCalculator = {
settings: {
  rowsDataName: 'formset_row',
  totalCostEl: document.querySelector('.order_total_cost'),
  totalQuantityEl: document.querySelector('.order_total_quantity'),
  tableEl: document.querySelector('table'),
  quantityDataSelector: 'data-quantity',
  priceDataSelector: 'data-price',
},
sumPrice: null,
sumQuantity: null,

init() {
  this.rowsWithDataInputs = this.settings.tableEl.querySelectorAll(`.${this.settings.rowsDataName}`);
  this.addListeners();
},

addListeners() {
  let quantityElems = document.querySelectorAll(`[${this.settings.quantityDataSelector}]`);
  for (let el of quantityElems) {
    if (!('listener' in el.dataset)) {
      el.setAttribute('listener', 'true');
      el.addEventListener('input', (event) => this.quantityListener(event));
    }
  }
},

quantityListener(event) {
  let quantity = event.target.value;
  event.target.parentElement.setAttribute(`${this.settings.quantityDataSelector}`, quantity);
  this.calculateSum();
  this.renderSum();
},

calculateSum() {
  this.setNullSum();
  for (let row of this.rowsWithDataInputs) {
    try {
      let price = row.querySelector(`[${this.settings.priceDataSelector}]`).dataset.price;
      let quantity = row.querySelector(`[${this.settings.quantityDataSelector}]`).dataset.quantity;
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


$('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        added: sumCalculator.addListeners()
    });